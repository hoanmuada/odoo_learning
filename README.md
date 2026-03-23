# Odoo (Development Environment for Learning)

## 🚀 Quick Start Guide
- **Start the Server**: Run `./start.sh` in the terminal.
- **Access Web UI**: Open http://localhost:8069 in your browser.

### 🔑 Credentials
- **Database**: `odoo_dev` (preloaded with Demo Data)
- **Email/Login**: `admin`
- **Password**: `admin`
- **Master Password**: `kdb9-b3km-gxi4` (used for creating/restoring DBs in Database Manager)

---

## Setup from Scratch

```bash
# 1. Clone Odoo 18
git clone https://github.com/odoo/odoo.git --depth 1 --branch 18.0

# 2. Install system deps (macOS)
brew install libxml2 libxslt libjpeg zlib

# 3. Create virtualenv
python3 -m venv venv
source venv/bin/activate
pip install "setuptools<75" wheel
PIP_CONSTRAINT=<(echo 'setuptools<75') pip install -r requirements.txt

# 4. PostgreSQL
createuser -s odoo

# 5. Start
./start.sh
```
