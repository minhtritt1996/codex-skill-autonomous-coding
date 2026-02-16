# Codex Skill: Autonomous Coding

Skill này port từ mẫu `anthropics/claude-quickstarts/autonomous-coding` để chạy tương thích với **Codex CLI**.

## Nội dung chính

- Runner tương thích Codex: `assets/upstream/codex_autonomous_demo.py`
- Script bootstrap project: `scripts/bootstrap.sh`
- Metadata skill: `SKILL.md`, `agents/openai.yaml`

## Cài đặt nhanh

Xem file: [INSTALL.md](INSTALL.md)

## Chạy thử sau khi cài skill

```bash
bash ~/.codex/skills/autonomous-coding/scripts/bootstrap.sh --target ./autonomous-coding
cd ./autonomous-coding
python codex_autonomous_demo.py --project-dir ./my_project --max-iterations 1
```

Bỏ `--max-iterations` để chạy vòng lặp tiếp tục tự động.
