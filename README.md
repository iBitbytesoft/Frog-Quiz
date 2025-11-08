# Frog Quiz Educational App 🐸

An interactive educational app teaching users about Australian frog species using spectrograms to visualize their calls.

## Features

- **8 Frog Species** with photos, videos, and audio spectrograms
- **Mystery Frog Quiz** - randomly selected frog call identification game
- **Instructions Page** - explains how spectrograms visualize sound
- **Landscape Mode** - optimized for tablets
- **Triple-tap Exit** - tap top-left corner 3 times to exit (Android)
- **Offline Support** - all assets embedded in APK

## Running Locally (Desktop)

### Prerequisites
- Python 3.9 or higher
- pip

### Installation

```powershell
# Install dependencies
pip install -r requirements.txt

# Run the app
python main.py
```

Access the app at: http://localhost:8080

## Deployment Options

### Option 1: Android APK (Offline - for schools)

#### Using GitHub Actions (Recommended - No Local Setup)

1. **Push code to GitHub:**
   ```powershell
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/frog-quiz.git
   git push -u origin main
   ```

2. **Enable GitHub Actions:**
   - Go to your repository on GitHub
   - Click "Actions" tab
   - The workflow will automatically start building
   - Wait ~15-30 minutes for the build to complete

3. **Download APK:**
   - Go to the completed workflow run
   - Download the "frog-quiz-apk" artifact
   - Extract the ZIP file
   - Transfer the `.apk` file to your Android tablet

4. **Install on Android:**
   - Enable "Install from Unknown Sources" in Settings
   - Open the APK file on the tablet
   - Install the app

#### Alternative: Local Build (Requires Linux/WSL)

```bash
# Install Buildozer
pip install buildozer

# Build APK
buildozer android debug

# APK will be in bin/ folder
```

### Option 2: iOS/iPad (Hosted - for exhibition)

**⚠️ NiceGUI cannot run on Vercel** (no WebSocket support)

Use one of these platforms instead:

#### Render.com (Free - Recommended)

1. Sign up at https://render.com
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Render will auto-detect `render.yaml` configuration
5. Click "Create Web Service"
6. Your app will be live at: `https://frog-quiz.onrender.com`

#### Railway.app (Easy Deployment)

1. Sign up at https://railway.app
2. Click "New Project" → "Deploy from GitHub"
3. Select your repository
4. Railway will auto-detect and deploy
5. Add a custom domain or use the Railway URL

#### Fly.io (Global Edge Network)

```bash
# Install flyctl
powershell -Command "iwr https://fly.io/install.ps1 -useb | iex"

# Login and deploy
fly auth login
fly launch
fly deploy
```

### Option 3: Docker (Self-hosted)

```bash
# Build image
docker build -t frog-quiz .

# Run container
docker run -p 8080:8080 frog-quiz
```

## Project Structure

```
NiceGUI/
├── main.py                 # Main application file
├── main_activity.py        # Android WebView integration
├── buildozer.spec          # Android build configuration
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker deployment
├── render.yaml             # Render.com configuration
├── assets/                 # Images and videos
│   ├── *.png              # Frog photos and UI elements
│   └── *_resized.mp4      # Frog call videos with spectrograms
└── .github/
    └── workflows/
        └── build-apk.yml   # GitHub Actions APK builder

```

## Client Requirements

- **Android APK**: Needed by Sunday (standalone, no internet)
- **iOS Web App**: Needed by Wednesday (hosted, requires internet)

## Key Features Implementation

✅ Triple-tap exit (top-left corner on home page)  
✅ Full-page automatic window resizing  
✅ Landscape orientation lock  
✅ Try Again button (resets quiz, random frog selection)  
✅ Video preloading without autoplay  
✅ Play/Pause button controls  
✅ Home navigation from all pages  

## Technologies

- **NiceGUI** - Python web framework
- **FastAPI** - Web server backend
- **Uvicorn** - ASGI server
- **Buildozer** - Android APK builder
- **Kivy** - Android runtime support

## Credits

App developed by Katie Howard for the exhibition *"Litoria's Wetland World"*

Sound files: Arthur Rylah Institute for Environmental Research (DEECA)  
Spectrograms: Created using PASE (Python-Audio-Spectrogram-Explorer)  
Photos: Katie Howard, Zak Atkins, Geoff Heard

## Troubleshooting

### APK Build Fails
- Check GitHub Actions logs for specific errors
- Ensure all assets are under 100MB total
- Videos should be compressed (use `_resized.mp4` versions)

### App won't install on Android
- Enable "Install from Unknown Sources"
- Check Android version (minimum API 28 / Android 9)
- Try uninstalling old version first

### Web deployment not working
- Verify requirements.txt includes all dependencies
- Check platform logs for errors
- Ensure port 8080 is configured correctly

## License

Educational use for school exhibitions and visits.
