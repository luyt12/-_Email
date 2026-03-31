# POLITICO Daily Email

Automated daily email digest of POLITICO news, translated to Chinese via Kimi K2.5 AI.

## How It Works

1. Fetches latest articles from POLITICO RSS feeds
2. Translates content to Chinese using Kimi K2.5 (NVIDIA API)
3. Sends a formatted HTML email daily

## Schedule

Runs automatically every day at 03:00 UTC via GitHub Actions.

## Setup

### Required GitHub Secrets

| Secret | Description |
|--------|-------------|
| `KIMI_API_KEY` | Kimi K2.5 API key (NVIDIA endpoint) |
| `SMTP_PASS` | SMTP password / app password |
| `EMAIL_TO` | Recipient email address |
| `EMAIL_FROM` | Sender email address |
| `SMTP_HOST` | SMTP server hostname |
| `SMTP_PORT` | SMTP server port |
| `SMTP_USER` | SMTP login username |

### Manual Trigger

Go to **Actions** tab → **Daily POLITICO News Email** → **Run workflow**.

## Tech Stack

- Python 3.11
- GitHub Actions (scheduled)
- Kimi K2.5 via NVIDIA API
- SMTP over TLS (port 465)
