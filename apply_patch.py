import sys

# Read the file
with open("index.html", "r", encoding="utf-8") as fh:
    content = fh.read()

changes = 0

if 'github: "https://github.com/dbwjdtn10/Npcdialogueengine"' in content:
    content = content.replace('github: "https://github.com/dbwjdtn10/Npcdialogueengine"', 'github: "https://github.com/dbwjdtn10/NpcDialogueEngine"')
    changes += 1
    print("Applied fix")
else:
    print("WARNING: Could not find pattern to replace")

if 'github: "https://github.com/dbwjdtn10/AI_Arena"' in content:
    content = content.replace('github: "https://github.com/dbwjdtn10/AI_Arena"', 'github: "https://github.com/dbwjdtn10/ai-arena"')
    changes += 1
    print("Applied fix")
else:
    print("WARNING: Could not find pattern to replace")

if 'github: "https://github.com/dbwjdtn10/Procedural-Quest-Writer"' in content:
    content = content.replace('github: "https://github.com/dbwjdtn10/Procedural-Quest-Writer"', 'github: "https://github.com/dbwjdtn10/procedural-quest-writer"')
    changes += 1
    print("Applied fix")
else:
    print("WARNING: Could not find pattern to replace")

if 'github: "https://github.com/dbwjdtn10/AI-email-triage"' in content:
    content = content.replace('github: "https://github.com/dbwjdtn10/AI-email-triage"', 'github: "https://github.com/dbwjdtn10/ai-email-triage"')
    changes += 1
    print("Applied fix")
else:
    print("WARNING: Could not find pattern to replace")

if 'github: "https://github.com/dbwjdtn10/LocalDocs"' in content:
    content = content.replace('github: "https://github.com/dbwjdtn10/LocalDocs"', 'github: "https://github.com/dbwjdtn10/localdocs"')
    changes += 1
    print("Applied fix")
else:
    print("WARNING: Could not find pattern to replace")

if '    { title: "FinalBite (Unity)", desc: "뱀서라이크 모바일 게임 — Google Play 출시 준비", tags: ["Unity 6.3", "Mobile", "IAP"], github: "https://github.com/dbwjdtn10/FinalBite" },\n    { title: "StoryProof", desc: "AI 소설 분석/창작 플랫폼 — 4인 팀 팀장 (6주)", tags: ["RAG", "Celery", "Team Lead"], github: "https://github.com/dbwjdtn10/StoryProof" },\n    { title: "LocalDocs", desc: "Tauri 2.0 + Rust 로컬 AI 문서 어시스턴트", tags: ["Tauri", "Rust", "Ollama"], github: "https://github.com/dbwjdtn10/localdocs" },\n    ];' in content:
    content = content.replace('    { title: "FinalBite (Unity)", desc: "뱀서라이크 모바일 게임 — Google Play 출시 준비", tags: ["Unity 6.3", "Mobile", "IAP"], github: "https://github.com/dbwjdtn10/FinalBite" },\n    { title: "StoryProof", desc: "AI 소설 분석/창작 플랫폼 — 4인 팀 팀장 (6주)", tags: ["RAG", "Celery", "Team Lead"], github: "https://github.com/dbwjdtn10/StoryProof" },\n    { title: "LocalDocs", desc: "Tauri 2.0 + Rust 로컬 AI 문서 어시스턴트", tags: ["Tauri", "Rust", "Ollama"], github: "https://github.com/dbwjdtn10/localdocs" },\n    ];', '    { title: "StoryProof", desc: "AI 소설 분석/창작 플랫폼 — 4인 팀 팀장 (6주)", tags: ["RAG", "Celery", "Team Lead"], github: "https://github.com/dbwjdtn10/StoryProof" },\n    { title: "MindStep", desc: "AI 페르소나 기반 행동 코칭 플랫폼 — 팀장 (1주)", tags: ["FastAPI", "Gemini", "ACT/CBT"], github: "https://github.com/dbwjdtn10/mindstep" },\n    { title: "AutoTranslater", desc: "Claude API 기반 한국어 ↔ 영어 자동 문서 번역 도구", tags: ["Claude API", "Python"], github: "https://github.com/dbwjdtn10/AutoTranslater" },\n    { title: "LocalDocs", desc: "Tauri 2.0 + Rust 로컬 AI 문서 어시스턴트", tags: ["Tauri", "Rust", "Ollama"], github: "https://github.com/dbwjdtn10/localdocs" },\n    { title: "SmartClip", desc: "AI 웹 클리퍼 Chrome 확장 — 요약/태깅/대화", tags: ["Chrome Extension", "Ollama"], github: "https://github.com/dbwjdtn10/smartclip" },\n    { title: "CliChat", desc: "Rust + ratatui TUI 터미널 Ollama 채팅 클라이언트", tags: ["Rust", "ratatui", "Tokio"], github: "https://github.com/dbwjdtn10/clichat" },\n    { title: "OllaBot", desc: "discord.py + Ollama 로컬 LLM Discord AI 챗봇", tags: ["discord.py", "Ollama"], github: "https://github.com/dbwjdtn10/ollabot" },\n    { title: "Ocean Survivor", desc: "2D 벽돌깨기 어드벤처 게임 — Unity 팀프로젝트", tags: ["Unity", "C#", "WebGL"], github: "https://github.com/bupomya/OceanSurvivor" },\n    ];')
    changes += 1
    print("Applied fix")
else:
    print("WARNING: Could not find pattern to replace")


print(f"\nTotal changes applied: {changes}")

with open("index.html", "w", encoding="utf-8") as fh:
    fh.write(content)

print("Saved index.html")
