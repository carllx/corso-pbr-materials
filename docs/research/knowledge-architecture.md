# 项目知识架构与边界规范

本文档记录 `corso-pbr-materials`（三维数字材质制作）项目的“两层 Notebook”知识架构设计及其与代码仓库之间的权威边界。

## 1. 架构概述

本项目采用**两层 Notebook**知识架构，而不是将所有资料集中在单一 Notebook 中：

```
                    ┌────────────────────────────────────────────────────────┐
                    │                      代码仓库                           │
                    │               (Project Authority / 最终事实权威)         │
                    └───────────────────────────▲────────────────────────────┘
                                                │ 经过审核的研究结论、
                                                │ 课程判断与设计决定沉淀
                                                │
                 ┌──────────────────────────────┴──────────────────────────────┐
                 │                                                             │
┌────────────────┴────────────────────────┐       ┌────────────────────────────┴────────────────────────┐
│      Course Knowledge Notebook          │       │           AI Creative Workflow Notebook             │
│      (课程领域知识研究库)                │       │           (跨课程共享 AI 创作工作流)                 │
│ Locator: e29f9644-03b2-4e1b-bcb0-...   │       │ Locator: 20a99ba1-092f-40fe-9317-...                │
└─────────────────────────────────────────┘       └─────────────────────────────────────────────────────┘
```

## 2. 知识库分工

### 2.1 Course Knowledge Notebook
- **定位**：服务于《三维数字材质制作》课程自身的领域知识研究。
- **范围**：PBR 基础理论、游戏材质制作、UV、Baking、Texture / Material / Shader、Blender、Substance Painter、Substance Designer、Unreal / Unity、国内外权威教材、成熟课程、官方文档与教学资料。
- **定位约束**：这是课程自身的领域知识库，不应被定义为 AI-native Game Art Notebook。

### 2.2 AI Creative Workflow Notebook
- **定位**：跨多个课程共享的外部 AI 创作工作流研究空间。
- **范围**：AI Game Art、AI Animation / Film、AI Character / Visual Development、AI 3D、AI Material / Texture、AI Video、创作者与实际 production workflow、新模型、新工具及工作方法。
- **拆分策略**：目前保持统一，不进一步拆分成 AI Game Notebook 与 AI Animation Notebook。仅在未来满足以下条件时重新评估：
  1. 两个领域来源高度分化；
  2. 检索噪声明显影响研究；
  3. 游戏和动画已经形成各自稳定、独立的方法体系。

## 3. 知识边界与约束原则

1. **事实权威在仓库（Project Authority）**：
   NotebookLM 是用于 source discovery、检索、方案对比与知识综合的研究环境，并非项目的最终事实权威。被项目采纳的重要研究结论、课程判断与设计决定，必须沉淀回代码仓库中。
2. **资料无需冗余复制**：
   两个 Notebook 职责独立，不要求互相复制相同材料。
3. **凭据安全**：
   仓库中不保存任何 NotebookLM cookie、token、storage state 或其他凭据。
