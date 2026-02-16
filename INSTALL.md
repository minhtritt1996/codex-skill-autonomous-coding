# Installation Guide

## 1. Prerequisites

```bash
codex --help
python3 --version
git --version
```

## 2. Install skill vào Codex CLI (manual)

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/minhtritt1996/codex-skill-autonomous-coding.git /tmp/codex-skill-autonomous-coding
rm -rf ~/.codex/skills/autonomous-coding
cp -a /tmp/codex-skill-autonomous-coding ~/.codex/skills/autonomous-coding
```

## 2b. Install bằng skill-installer (1 lệnh)

Nếu môi trường Codex của bạn có sẵn script installer:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --url https://github.com/minhtritt1996/codex-skill-autonomous-coding/tree/master
```

Nếu repo dùng branch mặc định `main` thì đổi `master` thành `main`.

## 3. Verify skill structure

```bash
ls -la ~/.codex/skills/autonomous-coding
```

Bạn cần thấy các file/thư mục chính:

- `SKILL.md`
- `scripts/bootstrap.sh`
- `assets/upstream/codex_autonomous_demo.py`

## 4. Restart Codex

Thoát Codex CLI rồi mở lại để nhận skill mới.

## 5. Test end-to-end

```bash
bash ~/.codex/skills/autonomous-coding/scripts/bootstrap.sh --target ./autonomous-coding
cd ./autonomous-coding
python codex_autonomous_demo.py --project-dir ./my_project --max-iterations 1
```

## 6. Update skill về sau

```bash
cd /tmp/codex-skill-autonomous-coding
git pull
rm -rf ~/.codex/skills/autonomous-coding
cp -a /tmp/codex-skill-autonomous-coding ~/.codex/skills/autonomous-coding
```

Sau mỗi lần update: restart Codex.
