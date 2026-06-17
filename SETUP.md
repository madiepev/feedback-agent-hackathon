# Setup Guide

Before the hackathon begins, make sure you have the following tools installed and configured.

---

## Prerequisites Checklist

- [ ] GitHub account
- [ ] VS Code installed
- [ ] GitHub Copilot extension installed
- [ ] Git installed (for cloning repositories)
- [ ] Signed into GitHub in VS Code

---

## Step 1: Create a GitHub Account

If you don't have a GitHub account yet:

1. Go to [github.com/signup](https://github.com/signup)
2. Follow the signup process
3. Verify your email address

---

## Step 2: Enable GitHub Copilot

1. Go to [github.com/features/copilot](https://github.com/features/copilot)
2. Click **Start free trial** if you don't have access
3. Complete the signup process

**Note:** GitHub Copilot requires a subscription, but offers a free trial for new users.

---

## Step 3: Install VS Code

### Windows:
1. Go to [code.visualstudio.com](https://code.visualstudio.com)
2. Click **Download for Windows**
3. Run the installer
4. Follow the installation wizard (use default settings)
5. Launch VS Code

### macOS:
1. Go to [code.visualstudio.com](https://code.visualstudio.com)
2. Click **Download for Mac**
3. Open the downloaded `.zip` file
4. Drag **Visual Studio Code.app** to your **Applications** folder
5. Launch VS Code from Applications

### Linux:
1. Go to [code.visualstudio.com](https://code.visualstudio.com)
2. Click **Download** and select your Linux distribution
3. Follow the installation instructions for your package manager
4. Launch VS Code

---

## Step 4: Install Git

Git is required to clone and sync repositories with GitHub.

### Check if Git is Already Installed:

Open a terminal (Command Prompt on Windows, Terminal on Mac/Linux) and type:

```bash
git --version
```

If you see a version number (e.g., `git version 2.40.0`), Git is already installed. **Skip to Step 5.**

### Install Git:

**Windows:**
1. Go to [git-scm.com/download/win](https://git-scm.com/download/win)
2. Download and run the installer
3. Use default settings (or customize if you know what you're doing)
4. Restart VS Code after installation

**macOS:**
1. Open **Terminal**
2. Type: `git --version`
3. If Git is not installed, macOS will prompt you to install Command Line Tools
4. Follow the prompts to install

**Linux:**
```bash
# Debian/Ubuntu
sudo apt-get install git

# Fedora
sudo dnf install git

# Arch
sudo pacman -S git
```

---

## Step 5: Install GitHub Copilot Extension in VS Code

1. Open **VS Code**
2. Click the **Extensions** icon in the left sidebar (or press `Ctrl+Shift+X` / `Cmd+Shift+X`)
3. Search for **"GitHub Copilot"**
4. Click **Install** on the official "GitHub Copilot" extension by GitHub
5. Also install **"GitHub Copilot Chat"** extension
6. VS Code may prompt you to sign in to GitHub — click **Sign In** and authorize

---

## Step 6: Sign Into GitHub in VS Code

1. In VS Code, click the **Accounts** icon in the bottom-left corner (or status bar)
2. Click **Sign in with GitHub**
3. A browser window will open — authorize VS Code to access your GitHub account
4. Return to VS Code — you should now see your GitHub username

---

## Step 7: Fork and Clone the Hackathon Repository

You'll do this during **Phase 1** of the hackathon, but here's a preview:

### Fork the Repository (via GitHub Web):
1. Navigate to the hackathon repository on GitHub
2. Click **Fork** (top-right corner)
3. Select your account as the destination
4. Click **Create fork**

### Clone Your Fork in VS Code:
1. In VS Code, press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)
2. Type **"Git: Clone"** and select it
3. Paste your forked repository URL (e.g., `https://github.com/YOUR-USERNAME/feedback-agent-hackathon`)
4. Choose a folder on your computer to save the repository
5. Click **Open** when prompted to open the cloned repository

**Alternative (simpler):**
1. Open your forked repository on GitHub
2. Click the green **Code** button
3. Click **Open with GitHub Desktop** or **Open with Visual Studio Code**
4. Follow the prompts

---

## Step 8: Test Your Setup

1. Open **VS Code**
2. Open your cloned repository folder
3. Click the **GitHub Copilot Chat** icon in the left sidebar (or press `Ctrl+Alt+I` / `Cmd+Alt+I`)
4. Type: `Hello, are you working?`
5. If Copilot responds, you're all set! ✅

---

## Troubleshooting

### "Git not found" error in VS Code
- Make sure Git is installed (Step 4)
- Restart VS Code after installing Git
- Check that Git is in your system PATH

### "Sign in to use GitHub Copilot" message
- Click the sign-in prompt in VS Code
- Authorize VS Code to access your GitHub account
- Make sure your GitHub Copilot subscription is active

### Copilot not responding
- Check that both **GitHub Copilot** and **GitHub Copilot Chat** extensions are installed
- Sign out and sign back in to GitHub in VS Code
- Restart VS Code

### Can't clone repository
- Make sure you've forked the repository first (on GitHub web)
- Check that you're signed into GitHub in VS Code
- Verify your GitHub account has access to the repository

---

## Alternative: Use GitHub Web Interface Only

If you can't install VS Code or Git, you can participate using only the **GitHub web interface**:

- ✅ Fork the repository
- ✅ Create and edit instruction files directly on GitHub
- ✅ Commit changes
- ❌ **Cannot test your agent with Copilot Chat** (requires VS Code)

You can still design and share your agent, but you won't be able to test it yourself before cross-testing in Phase 3.

---

## Need Help?

- Ask a facilitator during the event
- Check the VS Code documentation: [code.visualstudio.com/docs](https://code.visualstudio.com/docs)
- Check the Git documentation: [git-scm.com/doc](https://git-scm.com/doc)

---

**Ready?** Return to [Phase 1: Orientation](phase1-orientation.md) to begin the hackathon.
