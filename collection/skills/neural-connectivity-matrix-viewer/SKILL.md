---
name: neural-connectivity-matrix-viewer
description: 脑连接矩阵交互式可视化工具。基于HTML5/JavaScript的浏览器端应用，支持EEG、ECoG、MEG、fMRI等高维神经连接数据的3D堆叠矩阵可视化，实时交互探索连接模式。适用于脑连接分析、神经数据可视化、连接组学。触发词：脑连接可视化、连接矩阵、神经网络可视化、connectivity matrix、brain connectivity visualization、EEG connectivity、MEG connectivity。
user-invocable: true
---

# 神经连接矩阵交互式可视化工具

**来源论文：** arXiv:1702.06405 - Interactive Web Application for Exploring Matrices of Neural Connectivity

## 核心方法论

基于浏览器的轻量级脑连接矩阵可视化框架：

### 1. 3D 堆叠矩阵可视化

将高维连接矩阵以 3D 形式展示：
- X轴：源脑区
- Y轴：目标脑区
- Z轴：连接强度/属性维度

### 2. 多维度同步展示

同时可视化多个连接属性：
- 连接强度
- 连接类型（功能/结构）
- 时频特征
- 统计显著性

### 3. 交互式探索

实时操作和筛选：
- 阈值调节
- 节点选择
- 子网络提取
- 动态旋转/缩放

## Python 实现

```python
import numpy as np
import json
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
from pathlib import Path
import webbrowser
import http.server
import socketserver
from threading import Thread
import time


@dataclass
class ConnectivityData:
    """连接数据结构"""
    matrix: np.ndarray           # 连接矩阵 (n x n)
    node_labels: List[str]       # 节点标签
    node_positions: np.ndarray   # 节点3D位置 (n x 3)
    edge_attributes: Dict[str, np.ndarray]  # 边属性
    metadata: Dict               # 元数据


class NeuralConnectivityMatrixViewer:
    """神经连接矩阵可视化器"""
    
    def __init__(self, data: ConnectivityData):
        """
        Args:
            data: 连接数据
        """
        self.data = data
        self.n_nodes = data.matrix.shape[0]
        
    def to_json(self, output_path: str = None) -> str:
        """转换为JSON格式
        
        Args:
            output_path: 输出文件路径
            
        Returns:
            json_str: JSON字符串
        """
        # 构建JSON结构
        json_data = {
            'nodes': [],
            'edges': [],
            'metadata': self.data.metadata
        }
        
        # 节点
        for i in range(self.n_nodes):
            node = {
                'id': i,
                'label': self.data.node_labels[i],
                'position': self.data.node_positions[i].tolist() if self.data.node_positions is not None else [0, 0, 0]
            }
            json_data['nodes'].append(node)
            
        # 边
        for i in range(self.n_nodes):
            for j in range(self.n_nodes):
                if i != j and self.data.matrix[i, j] != 0:
                    edge = {
                        'source': i,
                        'target': j,
                        'weight': float(self.data.matrix[i, j])
                    }
                    # 添加额外属性
                    for attr_name, attr_matrix in self.data.edge_attributes.items():
                        edge[attr_name] = float(attr_matrix[i, j])
                    json_data['edges'].append(edge)
                    
        json_str = json.dumps(json_data, indent=2)
        
        if output_path:
            with open(output_path, 'w') as f:
                f.write(json_str)
                
        return json_str
    
    def generate_html_viewer(self, output_path: str = 'viewer.html',
                             port: int = 8000) -> str:
        """生成HTML可视化页面
        
        Args:
            output_path: HTML输出路径
            port: 本地服务器端口
            
        Returns:
            html_path: HTML文件路径
        """
        html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Neural Connectivity Matrix Viewer</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.7.0/chart.min.js"></script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: Arial, sans-serif;
            background: #1a1a2e;
            color: #eee;
            overflow: hidden;
        }
        #container {
            display: flex;
            height: 100vh;
        }
        #sidebar {
            width: 300px;
            background: #16213e;
            padding: 20px;
            overflow-y: auto;
        }
        #viewer {
            flex: 1;
            position: relative;
        }
        #canvas3d {
            width: 100%;
            height: 100%;
        }
        h1 { font-size: 1.2em; margin-bottom: 20px; color: #4fc3f7; }
        .control-group { margin-bottom: 20px; }
        .control-group label { 
            display: block; 
            margin-bottom: 5px;
            font-size: 0.9em;
            color: #90caf9;
        }
        input[type="range"] {
            width: 100%;
            accent-color: #4fc3f7;
        }
        input[type="file"] {
            width: 100%;
            padding: 10px;
            background: #0f3460;
            border: none;
            color: #eee;
            cursor: pointer;
        }
        select {
            width: 100%;
            padding: 8px;
            background: #0f3460;
            border: none;
            color: #eee;
        }
        .stats {
            background: #0f3460;
            padding: 15px;
            border-radius: 5px;
            margin-top: 20px;
        }
        .stats h3 { font-size: 0.9em; margin-bottom: 10px; color: #4fc3f7; }
        .stat-item { 
            display: flex; 
            justify-content: space-between;
            font-size: 0.85em;
            margin-bottom: 5px;
        }
        .color-scale {
            display: flex;
            height: 20px;
            margin-top: 10px;
            border-radius: 3px;
        }
        .color-scale div { flex: 1; }
        #matrix2d {
            position: absolute;
            bottom: 20px;
            right: 20px;
            width: 200px;
            height: 200px;
            background: rgba(22, 33, 62, 0.9);
            border-radius: 5px;
            padding: 10px;
        }
        #matrix2d canvas {
            width: 100% !important;
            height: 100% !important;
        }
    </style>
</head>
<body>
    <div id="container">
        <div id="sidebar">
            <h1>Neural Connectivity Viewer</h1>
            
            <div class="control-group">
                <label>Load Data (JSON)</label>
                <input type="file" id="fileInput" accept=".json">
            </div>
            
            <div class="control-group">
                <label>Threshold: <span id="thresholdValue">0.0</span></label>
                <input type="range" id="threshold" min="0" max="1" step="0.01" value="0">
            </div>
            
            <div class="control-group">
                <label>Edge Width Scale</label>
                <input type="range" id="edgeWidth" min="0.1" max="5" step="0.1" value="1">
            </div>
            
            <div class="control-group">
                <label>Node Size</label>
                <input type="range" id="nodeSize" min="1" max="20" step="0.5" value="5">
            </div>
            
            <div class="control-group">
                <label>Color By</label>
                <select id="colorBy">
                    <option value="weight">Connection Weight</option>
                    <option value="strength">Node Strength</option>
                </select>
            </div>
            
            <div class="stats" id="stats">
                <h3>Network Statistics</h3>
                <div class="stat-item"><span>Nodes:</span><span id="statNodes">0</span></div>
                <div class="stat-item"><span>Edges:</span><span id="statEdges">0</span></div>
                <div class="stat-item"><span>Density:</span><span id="statDensity">0</span></div>
                <div class="stat-item"><span>Avg. Weight:</span><span id="statAvgWeight">0</span></div>
                <div class="color-scale" id="colorScale"></div>
            </div>
        </div>
        
        <div id="viewer">
            <div id="canvas3d"></div>
            <div id="matrix2d">
                <canvas id="matrixChart"></canvas>
            </div>
        </div>
    </div>
    
    <script>
        // Three.js 场景
        let scene, camera, renderer, controls;
        let nodes = [], edges = [];
        let connectivityData = null;
        let threshold = 0;
        
        function init() {
            // 场景
            scene = new THREE.Scene();
            scene.background = new THREE.Color(0x1a1a2e);
            
            // 相机
            camera = new THREE.PerspectiveCamera(60, 
                document.getElementById('canvas3d').clientWidth / 
                document.getElementById('canvas3d').clientHeight, 
                0.1, 1000);
            camera.position.set(0, 0, 100);
            
            // 渲染器
            renderer = new THREE.WebGLRenderer({ antialias: true });
            renderer.setSize(
                document.getElementById('canvas3d').clientWidth,
                document.getElementById('canvas3d').clientHeight
            );
            document.getElementById('canvas3d').appendChild(renderer.domElement);
            
            // 控制器
            controls = new THREE.OrbitControls(camera, renderer.domElement);
            controls.enableDamping = true;
            controls.dampingFactor = 0.05;
            
            // 光照
            const ambientLight = new THREE.AmbientLight(0x404040);
            scene.add(ambientLight);
            
            const directionalLight = new THREE.DirectionalLight(0xffffff, 0.5);
            directionalLight.position.set(1, 1, 1);
            scene.add(directionalLight);
            
            // 事件监听
            document.getElementById('fileInput').addEventListener('change', loadData);
            document.getElementById('threshold').addEventListener('input', updateThreshold);
            document.getElementById('edgeWidth').addEventListener('input', updateEdges);
            document.getElementById('nodeSize').addEventListener('input', updateNodes);
            document.getElementById('colorBy').addEventListener('change', updateColors);
            
            // 窗口大小调整
            window.addEventListener('resize', onWindowResize);
            
            animate();
        }
        
        function loadData(event) {
            const file = event.target.files[0];
            if (!file) return;
            
            const reader = new FileReader();
            reader.onload = function(e) {
                connectivityData = JSON.parse(e.target.result);
                createVisualization();
                updateStats();
                createMatrix2D();
            };
            reader.readAsText(file);
        }
        
        function createVisualization() {
            // 清除现有对象
            nodes.forEach(n => scene.remove(n));
            edges.forEach(e => scene.remove(e));
            nodes = [];
            edges = [];
            
            if (!connectivityData) return;
            
            // 创建节点
            connectivityData.nodes.forEach((node, i) => {
                const geometry = new THREE.SphereGeometry(5, 16, 16);
                const material = new THREE.MeshPhongMaterial({
                    color: 0x4fc3f7
                });
                const sphere = new THREE.Mesh(geometry, material);
                
                // 位置
                if (node.position && node.position.length === 3) {
                    sphere.position.set(...node.position);
                } else {
                    // 球形布局
                    const theta = (i / connectivityData.nodes.length) * Math.PI * 2;
                    const phi = Math.acos(2 * Math.random() - 1);
                    const r = 50;
                    sphere.position.set(
                        r * Math.sin(phi) * Math.cos(theta),
                        r * Math.sin(phi) * Math.sin(theta),
                        r * Math.cos(phi)
                    );
                }
                
                sphere.userData = { id: node.id, label: node.label };
                scene.add(sphere);
                nodes.push(sphere);
            });
            
            // 创建边
            connectivityData.edges.forEach(edge => {
                if (edge.weight < threshold) return;
                
                const source = nodes[edge.source];
                const target = nodes[edge.target];
                
                if (!source || !target) return;
                
                const points = [];
                points.push(source.position.clone());
                points.push(target.position.clone());
                
                const geometry = new THREE.BufferGeometry().setFromPoints(points);
                const material = new THREE.LineBasicMaterial({
                    color: getEdgeColor(edge.weight),
                    transparent: true,
                    opacity: Math.min(1, edge.weight * 2)
                });
                
                const line = new THREE.Line(geometry, material);
                line.userData = { weight: edge.weight };
                scene.add(line);
                edges.push(line);
            });
        }
        
        function getEdgeColor(weight) {
            // 颜色映射：蓝 -> 青 -> 绿 -> 黄 -> 红
            const colors = [
                [0.0, 0x2196f3],  // 蓝
                [0.25, 0x00bcd4], // 青
                [0.5, 0x4caf50],  // 绿
                [0.75, 0xffeb3b], // 黄
                [1.0, 0xf44336]   // 红
            ];
            
            for (let i = 0; i < colors.length - 1; i++) {
                if (weight >= colors[i][0] && weight < colors[i+1][0]) {
                    const t = (weight - colors[i][0]) / (colors[i+1][0] - colors[i][0]);
                    return interpolateColor(colors[i][1], colors[i+1][1], t);
                }
            }
            return colors[colors.length - 1][1];
        }
        
        function interpolateColor(c1, c2, t) {
            const r1 = (c1 >> 16) & 255;
            const g1 = (c1 >> 8) & 255;
            const b1 = c1 & 255;
            
            const r2 = (c2 >> 16) & 255;
            const g2 = (c2 >> 8) & 255;
            const b2 = c2 & 255;
            
            const r = Math.round(r1 + (r2 - r1) * t);
            const g = Math.round(g1 + (g2 - g1) * t);
            const b = Math.round(b1 + (b2 - b1) * t);
            
            return (r << 16) | (g << 8) | b;
        }
        
        function updateThreshold(event) {
            threshold = parseFloat(event.target.value);
            document.getElementById('thresholdValue').textContent = threshold.toFixed(2);
            createVisualization();
            updateStats();
        }
        
        function updateEdges(event) {
            const scale = parseFloat(event.target.value);
            edges.forEach(edge => {
                if (edge.material) {
                    edge.material.linewidth = scale;
                }
            });
        }
        
        function updateNodes(event) {
            const size = parseFloat(event.target.value);
            nodes.forEach(node => {
                node.scale.setScalar(size / 5);
            });
        }
        
        function updateColors(event) {
            const colorBy = event.target.value;
            // 根据选择更新颜色
            if (colorBy === 'strength') {
                // 计算节点强度
                const strengths = new Array(nodes.length).fill(0);
                if (connectivityData) {
                    connectivityData.edges.forEach(edge => {
                        if (edge.weight >= threshold) {
                            strengths[edge.source] += edge.weight;
                            strengths[edge.target] += edge.weight;
                        }
                    });
                }
                
                const maxStrength = Math.max(...strengths);
                nodes.forEach((node, i) => {
                    const intensity = strengths[i] / maxStrength;
                    node.material.color.setHex(getEdgeColor(intensity));
                });
            } else {
                nodes.forEach(node => {
                    node.material.color.setHex(0x4fc3f7);
                });
            }
        }
        
        function updateStats() {
            if (!connectivityData) return;
            
            const nNodes = connectivityData.nodes.length;
            const filteredEdges = connectivityData.edges.filter(e => e.weight >= threshold);
            const nEdges = filteredEdges.length;
            const maxEdges = nNodes * (nNodes - 1);
            const density = nEdges / maxEdges;
            const avgWeight = filteredEdges.reduce((sum, e) => sum + e.weight, 0) / nEdges || 0;
            
            document.getElementById('statNodes').textContent = nNodes;
            document.getElementById('statEdges').textContent = nEdges;
            document.getElementById('statDensity').textContent = density.toFixed(3);
            document.getElementById('statAvgWeight').textContent = avgWeight.toFixed(3);
        }
        
        function createMatrix2D() {
            if (!connectivityData) return;
            
            const n = connectivityData.nodes.length;
            const matrix = Array(n).fill(null).map(() => Array(n).fill(0));
            
            connectivityData.edges.forEach(edge => {
                matrix[edge.source][edge.target] = edge.weight;
            });
            
            const ctx = document.getElementById('matrixChart').getContext('2d');
            new Chart(ctx, {
                type: 'matrix',
                data: {
                    datasets: [{
                        label: 'Connectivity Matrix',
                        data: matrix.flatMap((row, i) => 
                            row.map((val, j) => ({ x: j, y: i, v: val }))
                        ),
                        backgroundColor(ctx) {
                            const value = ctx.dataset.data[ctx.dataIndex].v;
                            return `rgba(79, 195, 247, ${value})`;
                        },
                        width: ({ chart }) => chart.chartArea.width / n,
                        height: ({ chart }) => chart.chartArea.height / n
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: { display: false }
                    },
                    scales: {
                        x: { display: false },
                        y: { display: false }
                    }
                }
            });
        }
        
        function onWindowResize() {
            camera.aspect = document.getElementById('canvas3d').clientWidth / 
                           document.getElementById('canvas3d').clientHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(
                document.getElementById('canvas3d').clientWidth,
                document.getElementById('canvas3d').clientHeight
            );
        }
        
        function animate() {
            requestAnimationFrame(animate);
            controls.update();
            renderer.render(scene, camera);
        }
        
        init();
    </script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
</body>
</html>'''
        
        with open(output_path, 'w') as f:
            f.write(html_content)
            
        return output_path
    
    def launch_viewer(self, port: int = 8000):
        """启动本地可视化服务器
        
        Args:
            port: 服务器端口
        """
        # 生成HTML
        html_path = self.generate_html_viewer()
        
        # 保存JSON数据
        json_path = 'connectivity_data.json'
        self.to_json(json_path)
        
        # 启动服务器
        class Handler(http.server.SimpleHTTPRequestHandler):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, directory='.', **kwargs)
                
        with socketserver.TCPServer(("", port), Handler) as httpd:
            url = f"http://localhost:{port}/{html_path}"
            print(f"Viewer running at {url}")
            webbrowser.open(url)
            httpd.serve_forever()


def convert_matlab_to_json(matlab_file: str, output_file: str,
                           var_name: str = 'connectivity') -> str:
    """转换MATLAB数据为JSON
    
    Args:
        matlab_file: MATLAB文件路径
        output_file: 输出JSON路径
        var_name: 连接矩阵变量名
        
    Returns:
        json_path: JSON文件路径
    """
    try:
        import scipy.io as sio
    except ImportError:
        raise ImportError("scipy required for MATLAB file conversion")
        
    # 加载MATLAB文件
    mat_data = sio.loadmat(matlab_file)
    
    if var_name not in mat_data:
        raise ValueError(f"Variable '{var_name}' not found in MATLAB file")
        
    matrix = mat_data[var_name]
    n = matrix.shape[0]
    
    # 创建节点标签
    node_labels = [f"Node_{i}" for i in range(n)]
    
    # 创建默认位置（球形布局）
    positions = np.zeros((n, 3))
    for i in range(n):
        theta = (i / n) * 2 * np.pi
        phi = np.arccos(2 * (i / n) - 1)
        r = 50
        positions[i] = [
            r * np.sin(phi) * np.cos(theta),
            r * np.sin(phi) * np.sin(theta),
            r * np.cos(phi)
        ]
    
    # 创建数据结构
    data = ConnectivityData(
        matrix=matrix,
        node_labels=node_labels,
        node_positions=positions,
        edge_attributes={},
        metadata={
            'source': matlab_file,
            'n_nodes': n,
            'n_edges': np.count_nonzero(matrix)
        }
    )
    
    # 保存JSON
    viewer = NeuralConnectivityMatrixViewer(data)
    return viewer.to_json(output_file)


def create_eeg_connectivity_example(n_channels: int = 64,
                                   n_timepoints: int = 100) -> ConnectivityData:
    """创建EEG连接数据示例
    
    Args:
        n_channels: EEG通道数
        n_timepoints: 时间点数
        
    Returns:
        data: 连接数据
    """
    # 模拟EEG通道位置（10-20系统简化）
    positions = np.zeros((n_channels, 3))
    for i in range(n_channels):
        theta = (i / n_channels) * 2 * np.pi
        phi = np.pi / 3 + (i % 3) * np.pi / 6
        r = 50
        positions[i] = [
            r * np.sin(phi) * np.cos(theta),
            r * np.sin(phi) * np.sin(theta),
            r * np.cos(phi)
        ]
    
    # 模拟连接矩阵
    rng = np.random.default_rng(42)
    
    # 基础连接（距离衰减）
    dist_matrix = np.zeros((n_channels, n_channels))
    for i in range(n_channels):
        for j in range(n_channels):
            dist_matrix[i, j] = np.linalg.norm(positions[i] - positions[j])
    
    # 连接强度随距离衰减
    sigma = np.mean(dist_matrix[dist_matrix > 0]) / 3
    connectivity = np.exp(-dist_matrix**2 / (2 * sigma**2))
    
    # 添加模块化结构
    n_modules = 8
    module_size = n_channels // n_modules
    for m in range(n_modules):
        start = m * module_size
        end = min((m + 1) * module_size, n_channels)
        connectivity[start:end, start:end] *= 2
    
    # 归一化
    connectivity = connectivity / connectivity.max()
    
    # 移除对角线
    np.fill_diagonal(connectivity, 0)
    
    # 节点标签
    labels = [f"EEG_{i:02d}" for i in range(n_channels)]
    
    return ConnectivityData(
        matrix=connectivity,
        node_labels=labels,
        node_positions=positions,
        edge_attributes={
            'distance': dist_matrix,
            'phase_lag': rng.uniform(0, 2*np.pi, (n_channels, n_channels))
        },
        metadata={
            'modality': 'EEG',
            'n_channels': n_channels,
            'reference': 'average'
        }
    )


# 使用示例
def example_eeg_visualization():
    """示例：EEG连接可视化"""
    # 创建示例数据
    data = create_eeg_connectivity_example(n_channels=64)
    
    # 创建可视化器
    viewer = NeuralConnectivityMatrixViewer(data)
    
    # 保存JSON
    viewer.to_json('eeg_connectivity.json')
    print(f"Saved connectivity data with {data.matrix.shape[0]} nodes")
    print(f"Number of edges: {np.count_nonzero(data.matrix)}")
    
    # 生成HTML
    html_path = viewer.generate_html_viewer('eeg_viewer.html')
    print(f"HTML viewer saved to: {html_path}")
    
    # 启动服务器（可选）
    # viewer.launch_viewer(port=8000)
    
    return viewer


def example_from_matlab():
    """示例：从MATLAB文件加载"""
    # 假设有MATLAB文件
    # json_path = convert_matlab_to_json('connectivity.mat', 'connectivity.json')
    # viewer = NeuralConnectivityMatrixViewer(load_from_json(json_path))
    pass


## Activation Keywords
- 脑连接可视化
- 连接矩阵
- 神经网络可视化
- connectivity matrix
- brain connectivity visualization
- EEG connectivity
- MEG connectivity
- fMRI connectivity
- 3D matrix visualization
- interactive brain viewer

## Tools Used
- numpy
- json
- three.js (WebGL)
- Chart.js
- scipy (MATLAB conversion)

## Instructions for Agents
1. 数据准备：将连接矩阵转换为JSON格式
2. 加载数据：支持JSON文件或MATLAB数据转换
3. 交互探索：使用阈值调节、节点选择等功能
4. 多维度可视化：同时展示连接强度、距离等属性
5. 导出分享：生成独立的HTML文件

## Examples
```python
# EEG连接可视化示例
from neural_connectivity_matrix_viewer import NeuralConnectivityMatrixViewer, create_eeg_connectivity_example

# 1. 创建示例数据
data = create_eeg_connectivity_example(n_channels=64)

# 2. 创建可视化器
viewer = NeuralConnectivityMatrixViewer(data)

# 3. 保存JSON数据
viewer.to_json('eeg_connectivity.json')

# 4. 生成HTML可视化页面
viewer.generate_html_viewer('viewer.html')

# 5. 启动本地服务器（可选）
# viewer.launch_viewer(port=8000)
```

if __name__ == "__main__":
    viewer = example_eeg_visualization()
```

## Related Skills

- `brain-network-controllability` - 脑网络可控性分析
- `eeg-brain-connectivity-bci` - EEG脑连接BCI
- `multimodal-brain-connectivity-gnn` - 多模态脑连接GNN

## References

- arXiv:1702.06405 - Interactive Web Application for Exploring Matrices of Neural Connectivity
- IEEE NER 2017
- DOI: 10.1109/NER.2017.8008287