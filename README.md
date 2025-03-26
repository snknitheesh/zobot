Here's a clean, professional `README.md` for your project that explains the **devcontainer setup**, **Isaac Sim version handling**, and your custom `cm` command usage:

---

```markdown
# 🧠 Isaac Sim Devcontainer + ROS 2 Workspace

This project provides a devcontainer-based ROS 2 development environment with Isaac Sim integration.

## 📦 Features

- ✅ Devcontainer with volume-mounted cache for faster Isaac Sim startup
- ✅ Isaac Sim version can be changed per project
- ✅ ROS 2 Python package (`zobot`) to launch Isaac Sim via `ros2 launch`
- ✅ `cm` utility shortcuts for build/test/dependency setup

---

## 🚀 Getting Started

### 1. Clone this repository
```bash
git clone git@github.com:snknitheesh/artificial_intelligence.git
cd artificial_intelligence
```

---

### 2. Open in VS Code Devcontainer

> Requires [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

Click **“Reopen in Container”** when prompted, or open the Command Palette (`Ctrl+Shift+P`) and run:

```
Dev Containers: Rebuild and Reopen in Container
```

---

### 3. ✅ Change Isaac Sim Version

Inside `devcontainer.json`, you can switch versions by changing the ISAAC_SIM_VERSION:

```json
"build": {
  "args": {
    "ISAAC_SIM_VERSION": "[4.5 or 4.2]"
  }
}
```

Ensure the correct version is also reflected in your local `isaac_sim` install or cache folders.

---

## 🛠️ Custom Commands (`cm`)

This project includes a `cm` utility script for ROS 2 workflows.

| Command      | Description                      |
|--------------|----------------------------------|
| `cm`         | Alias for `colcon build`         |
| `cm test`    | Runs `colcon test`               |
| `cm dep`     | Installs ROS 2 dependencies via `rosdep` |

```bash
# Build the workspace
cm

# Run tests
cm test

# Install dependencies
cm dep
```

---

## 🧪 Running Isaac Sim


To build the ros packages:
```bash
cm
```
To launch Isaac Sim with a cube already spawned:
```bash
ros2 launch zobot isaac.launch.py
```

This will:
- Start Isaac Sim with GUI
- Load a minimal scene
- Spawn a basic colored cube at `/World/Cube`

---

## 📚 Troubleshooting

### Isaac Sim takes forever to start?
Make sure cache directories are mounted and writable.

## 📌 Requirements

- Docker
- VS Code + Dev Containers extension
- NVIDIA GPU (for Isaac Sim)
- Properly installed Isaac Sim SDK (outside container)

---

## 🧠 Maintained by

Nitheesh Kumar – [@snknitheesh](https://github.com/snknitheesh)

---
```
