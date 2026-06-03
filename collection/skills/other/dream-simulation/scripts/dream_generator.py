#!/usr/bin/env python3
"""
梦境生成器 - 基于神经科学研究的梦境叙事模拟
基于: Tavangari et al. (2025) 神经动力学模型
"""

import json
import random
from datetime import datetime
from dataclasses import dataclass
from typing import List, Dict, Optional


@dataclass
class MemoryFragment:
    """记忆片段 - 梦境的基本构建单元"""

    content: str
    emotional_valence: float  # -1.0 to 1.0
    intensity: float  # 0.0 to 1.0
    memory_type: str  # "event", "emotion", "sensory", "abstract"


@dataclass
class DreamParams:
    """梦境生成参数"""

    memory_decay: float = 0.7
    emotion_intensity: float = 0.8
    narrative_coherence: float = 0.4
    surrealism_level: float = 0.6
    lucidity_trigger: float = 0.3


class DreamGenerator:
    """梦境生成器 - 模拟 REM 睡眠期的认知过程"""

    # 梦境象征库
    DREAM_SYMBOLS = {
        "anxiety": ["坠落", "被追赶", "迟到", "考试", "牙齿脱落", "迷路"],
        "joy": ["飞翔", "庆祝", "阳光明媚", "与亲友相聚", "获得奖励"],
        "anger": ["战斗", "破坏", "风暴", "火山", "被困"],
        "sadness": ["失去", "离别", "下雨", "黑暗", "孤独行走"],
        "curiosity": ["探索", "发现", "迷宫", "书籍", "未知的门"],
        "stress": ["机器故障", "无法移动", "喊叫无声", "重复任务"],
    }

    # 梦境转换词
    TRANSITIONS = [
        "突然",
        "不知为何",
        "然后",
        "转眼间",
        "奇怪地",
        "不知不觉中",
        "仿佛",
        "像是在",
        "与此同时",
    ]

    # 超现实元素
    SURREAL_ELEMENTS = [
        "物体漂浮在空中",
        "重力消失",
        "时间倒流",
        "空间折叠",
        "物体改变颜色",
        "人可以穿过墙壁",
        "动物会说话",
        "建筑在生长",
        "镜子中的另一个世界",
    ]

    def __init__(self, params: Optional[DreamParams] = None):
        self.params = params or DreamParams()

    def encode_memories(self, daily_experiences: List[str]) -> List[MemoryFragment]:
        """Phase 1: 编码日间经历为记忆片段"""
        fragments = []

        for exp in daily_experiences:
            # 分析情感色彩 (简化版情感分析)
            emotional_valence = self._estimate_emotion(exp)
            intensity = random.uniform(0.5, 1.0)  # 近期记忆强度较高

            # 确定记忆类型
            if any(word in exp for word in ["感觉", "看到", "听到", "触摸"]):
                mem_type = "sensory"
            elif any(word in exp for word in ["开心", "难过", "生气", "害怕"]):
                mem_type = "emotion"
            elif any(word in exp for word in ["想", "认为", "觉得"]):
                mem_type = "abstract"
            else:
                mem_type = "event"

            fragments.append(
                MemoryFragment(
                    content=exp,
                    emotional_valence=emotional_valence,
                    intensity=intensity,
                    memory_type=mem_type,
                )
            )

        return fragments

    def _estimate_emotion(self, text: str) -> float:
        """估算文本情感值 (-1.0 to 1.0)"""
        positive = ["开心", "快乐", "成功", "喜欢", "爱", "满意", "放松"]
        negative = ["压力", "焦虑", "失败", "讨厌", "生气", "担心", "累"]

        pos_count = sum(1 for p in positive if p in text)
        neg_count = sum(1 for n in negative if n in text)

        if pos_count + neg_count == 0:
            return random.uniform(-0.2, 0.2)

        return (pos_count - neg_count) / max(pos_count + neg_count, 1)

    def consolidate_memories(
        self, fragments: List[MemoryFragment]
    ) -> List[MemoryFragment]:
        """Phase 2: 记忆巩固 - 随机激活和衰减"""
        # 应用记忆衰减
        consolidated = []
        for frag in fragments:
            if random.random() < self.params.memory_decay:
                # 情感强度影响记忆保留概率
                retention_prob = frag.intensity * (1 + abs(frag.emotional_valence))
                if random.random() < retention_prob:
                    consolidated.append(frag)

        # 随机重排序 (模拟海马体的索引重放)
        random.shuffle(consolidated)

        return consolidated

    def construct_narrative(self, fragments: List[MemoryFragment]) -> str:
        """Phase 3: 构建梦境叙事"""
        if not fragments:
            return "你睡得很沉，没有留下任何梦境记忆。"

        narrative_parts = []

        # 根据主导情感选择主题
        dominant_emotion = self._get_dominant_emotion(fragments)
        symbols = self.DREAM_SYMBOLS.get(
            dominant_emotion, self.DREAM_SYMBOLS["curiosity"]
        )

        # 构建场景
        narrative_parts.append(self._generate_opening(dominant_emotion))

        # 将记忆片段融入象征性叙事
        for i, frag in enumerate(fragments[:5]):  # 最多处理5个片段
            if random.random() < self.params.narrative_coherence:
                # 连贯叙事
                narrative_parts.append(
                    self._coherent_scene(frag, symbols[i % len(symbols)])
                )
            else:
                # 跳跃式叙事 (梦境特征)
                narrative_parts.append(self._surreal_transition())
                narrative_parts.append(self._incoherent_scene(frag))

            # 随机插入超现实元素
            if random.random() < self.params.surrealism_level:
                narrative_parts.append(random.choice(self.SURREAL_ELEMENTS))

        narrative_parts.append(self._generate_ending())

        return " ".join(narrative_parts)

    def _get_dominant_emotion(self, fragments: List[MemoryFragment]) -> str:
        """确定主导情感"""
        if not fragments:
            return "curiosity"

        avg_valence = sum(f.emotional_valence for f in fragments) / len(fragments)

        if avg_valence < -0.5:
            return "anxiety"
        elif avg_valence < -0.2:
            return "sadness"
        elif avg_valence > 0.5:
            return "joy"
        elif avg_valence > 0.2:
            return "curiosity"
        else:
            return "stress"

    def _generate_opening(self, emotion: str) -> str:
        """生成梦境开场"""
        openings = {
            "anxiety": ["你发现自己站在悬崖边缘", "有人在追赶你", "你迟到了"],
            "joy": ["你在阳光下飞翔", "周围是庆祝的人群", "你获得了大奖"],
            "sadness": ["你在雨中独自行走", "周围一片寂静", "你在寻找什么"],
            "curiosity": [
                "你发现了一扇神秘的门",
                "你进入了一个未知的世界",
                "你拿着一张古老的地图",
            ],
            "stress": [
                "机器在你身边嗡嗡作响",
                "你在无尽的走廊中奔跑",
                "时间在你眼前加速流逝",
            ],
        }
        return random.choice(openings.get(emotion, openings["curiosity"]))

    def _coherent_scene(self, fragment: MemoryFragment, symbol: str) -> str:
        """生成连贯场景"""
        transition = random.choice(self.TRANSITIONS)
        return f"{transition}，你遇到了{symbol}，让你想起{fragment.content[:20]}..."

    def _incoherent_scene(self, fragment: MemoryFragment) -> str:
        """生成不连贯场景 (梦境跳跃)"""
        surreal = random.choice(self.SURREAL_ELEMENTS)
        return (
            f"场景变换，{surreal}，你感到{fragment.emotional_valence:.1f}的情感波动。"
        )

    def _surreal_transition(self) -> str:
        """生成超现实转换"""
        return random.choice(self.TRANSITIONS)

    def _generate_ending(self) -> str:
        """生成梦境结尾"""
        endings = [
            "你渐渐醒来，梦境如烟雾般消散。",
            "一阵铃声响起，梦境戛然而止。",
            "你意识到自己在做梦，然后慢慢睁开眼睛。",
            "梦境淡出，留下淡淡的情感余韵。",
        ]
        return random.choice(endings)

    def generate_interpretation(self, fragments: List[MemoryFragment]) -> Dict:
        """生成神经科学解读"""
        dominant_emotion = self._get_dominant_emotion(fragments)

        interpretations = {
            "anxiety": {
                "mechanism": "杏仁核-海马体过度激活",
                "suggestion": "尝试睡前放松练习，降低皮质醇水平",
            },
            "joy": {
                "mechanism": "多巴胺奖赏系统的正向重放",
                "suggestion": "巩固这些积极记忆，有助于情绪调节",
            },
            "sadness": {
                "mechanism": "前额叶皮层情感调节活动",
                "suggestion": "允许情感释放，这是健康的处理机制",
            },
            "curiosity": {
                "mechanism": "默认模式网络 (DMN) 高活跃度",
                "suggestion": "创意高峰期，适合解决开放性问题",
            },
            "stress": {
                "mechanism": "交感神经系统的梦境延续",
                "suggestion": "关注压力源，建立更好的边界",
            },
        }

        return interpretations.get(dominant_emotion, interpretations["curiosity"])

    def generate_dream(self, daily_experiences: List[str]) -> Dict:
        """
        完整梦境生成流程

        Args:
            daily_experiences: 日间经历列表

        Returns:
            包含梦境叙事、解读和建议的字典
        """
        # Phase 1-3: 编码、巩固、构建
        fragments = self.encode_memories(daily_experiences)
        consolidated = self.consolidate_memories(fragments)
        narrative = self.construct_narrative(consolidated)
        interpretation = self.generate_interpretation(consolidated)

        # 检查清醒梦触发
        lucidity = random.random() < self.params.lucidity_trigger

        return {
            "timestamp": datetime.now().isoformat(),
            "narrative": narrative,
            "memory_fragments": len(consolidated),
            "dominant_emotion": self._get_dominant_emotion(consolidated),
            "interpretation": interpretation,
            "lucidity_triggered": lucidity,
            "parameters": {
                "memory_decay": self.params.memory_decay,
                "surrealism_level": self.params.surrealism_level,
            },
        }


def main():
    """命令行接口"""
    import sys

    if len(sys.argv) < 2:
        print("Usage: dream_generator.py '<experience1>' '<experience2>' ...")
        print("Example: dream_generator.py '今天工作压力很大' '中午吃了好吃的寿司'")
        sys.exit(1)

    experiences = sys.argv[1:]
    generator = DreamGenerator()
    dream = generator.generate_dream(experiences)

    print(json.dumps(dream, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
