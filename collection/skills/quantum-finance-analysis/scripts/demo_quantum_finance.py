#!/usr/bin/env python3
"""
量子金融分析演示脚本

基于知识图谱论文提取的模式：
1. 混合量子-经典架构
2. QUBO投资组合优化
3. 量子蒙特卡洛风险度量
"""

import numpy as np
from typing import List, Dict


class HybridQuantumPortfolio:
    """
    混合量子-经典投资组合优化器

    来源模式：Quantum Computing: Vision and Challenges
             FinRL-Podracer: High Performance DRL
    """

    def __init__(self, use_quantum=False):
        self.use_quantum = use_quantum
        self.classical_solver = "scipy.optimize"
        self.quantum_backend = None

    def optimize_portfolio(
        self,
        assets: List[str],
        returns: np.ndarray,
        cov_matrix: np.ndarray,
        risk_tolerance: float = 0.5,
    ) -> Dict:
        """
        投资组合优化

        Args:
            assets: 资产名称列表
            returns: 预期收益率数组
            cov_matrix: 协方差矩阵
            risk_tolerance: 风险容忍度 (0-1)

        Returns:
            最优权重分配
        """

        # Step 1: 经典预处理
        _ = len(assets)
        _ = np.mean(returns)

        # Step 2: QUBO 形式化（如使用量子）
        if self.use_quantum:
            _ = self._formulate_qubo(returns, cov_matrix, risk_tolerance)
            # 这里应调用量子求解器（QAOA/VQE）
            # weights = self._quantum_solve(qubo_matrix)
            weights = self._classical_solve(returns, cov_matrix)
        else:
            weights = self._classical_solve(returns, cov_matrix)

        # Step 3: 结果验证
        portfolio_return = np.dot(weights, returns)
        portfolio_risk = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        sharpe_ratio = portfolio_return / portfolio_risk

        return {
            "weights": weights,
            "expected_return": portfolio_return,
            "risk": portfolio_risk,
            "sharpe_ratio": sharpe_ratio,
        }

    def _formulate_qubo(self, returns, cov_matrix, risk_tol):
        """
        将 Markowitz 问题映射到 QUBO

        QUBO: min x^T Q x

        Q = Σ (variance) - μ (return) + λ (constraints)
        """
        n = len(returns)  # noqa: F841
        
        # QUBO 矩阵构建
        Q = risk_tol * cov_matrix - (1 - risk_tol) * np.diag(returns)

        return Q

    def _classical_solve(self, returns, cov_matrix):
        """
        经典求解器（作为量子求解器的替代或验证）
        """
        from scipy.optimize import minimize

        n = len(returns)

        def objective(w):
            portfolio_return = np.dot(w, returns)
            portfolio_risk = np.sqrt(np.dot(w.T, np.dot(cov_matrix, w)))
            return -portfolio_return / portfolio_risk  # 最大化夏普比率

        constraints = [
            {"type": "eq", "fun": lambda w: np.sum(w) - 1.0}  # 权重和为1
        ]
        bounds = [(0, 1) for _ in range(n)]  # 权重约束

        result = minimize(
            objective,
            np.ones(n) / n,  # 初始等权重
            method="SLSQP",
            bounds=bounds,
            constraints=constraints,
        )

        return result.x


class QuantumRiskMetrics:
    """
    量子增强风险度量

    来源模式：Quantum-Enhanced Monte Carlo for Risk
             Use Cases of Quantum Optimization for Finance
    """

    def __init__(self):
        self.use_qrng = False  # Quantum Random Number Generator

    def monte_carlo_var(
        self, portfolio_value: float, simulations: int = 10000, confidence: float = 0.95
    ) -> Dict:
        """
        Monte Carlo VaR 估计

        量子优势：振幅估计提供 O(√N) 加速
        """

        # 使用 QRNG 或经典随机数
        if self.use_qrng:
            random_samples = self._qrng_samples(simulations)
        else:
            random_samples = np.random.standard_normal(simulations)

        # 模拟损失分布
        losses = portfolio_value * random_samples

        # 计算 VaR
        var = np.percentile(losses, confidence * 100)
        cvar = np.mean(losses[losses >= var])

        return {
            "VaR": var,
            "CVaR": cvar,
            "confidence": confidence,
            "simulations": simulations,
        }

    def _qrng_samples(self, n):
        """
        QRNG 采样（实际应用需连接量子设备）
        """
        # 模拟 QRNG
        return np.random.standard_normal(n)


def demo_quantum_portfolio():
    """
    演示量子投资组合优化
    """

    # 示例数据
    assets = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]
    returns = np.array([0.12, 0.15, 0.10, 0.08, 0.20])  # 预期年收益率

    # 协方差矩阵（模拟）
    cov_matrix = np.array(
        [
            [0.04, 0.02, 0.01, 0.01, 0.03],
            [0.02, 0.06, 0.02, 0.01, 0.04],
            [0.01, 0.02, 0.03, 0.01, 0.02],
            [0.01, 0.01, 0.01, 0.02, 0.01],
            [0.03, 0.04, 0.02, 0.01, 0.10],
        ]
    )

    # 经典优化
    optimizer = HybridQuantumPortfolio(use_quantum=False)
    result = optimizer.optimize_portfolio(assets, returns, cov_matrix)

    print("=" * 60)
    print("量子金融分析演示")
    print("=" * 60)
    print("\n投资组合优化结果：")
    for i, asset in enumerate(assets):
        print(f"  {asset}: {result['weights'][i]:.2%}")

    print(f"\n预期收益率: {result['expected_return']:.2%}")
    print(f"风险 (标准差): {result['risk']:.2%}")
    print(f"夏普比率: {result['sharpe_ratio']:.3f}")

    # 风险度量
    risk_metrics = QuantumRiskMetrics()
    var_result = risk_metrics.monte_carlo_var(100000, 10000, 0.95)

    print("\n风险度量 (VaR):")
    print(f"  95% VaR: ${-var_result['VaR']:.2f}")
    print(f"  95% CVaR: ${-var_result['CVaR']:.2f}")
    print(f"  模拟次数: {var_result['simulations']}")

    print("\n" + "=" * 60)
    print("量子优势潜力：")
    print("  - QUBO 优化：量子退火/QAOA 可加速组合优化")
    print("  - 振幅估计：蒙特卡洛次数从 N 降至 √N")
    print("  - QRNG：真实随机性增强模拟精度")
    print("=" * 60)


if __name__ == "__main__":
    demo_quantum_portfolio()
