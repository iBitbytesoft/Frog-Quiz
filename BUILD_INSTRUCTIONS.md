# Build and Test Instructions for Updated Kivy APK

## Quick Summary of Changes

All client-requested fixes have been implemented:
1. ✅ Fixed home page button labels (no longer cutting off)
2. ✅ Added complete app info (photographer credits, full details)
3. ✅ Fixed button aspect ratios (now maintain square shape)
4. ✅ Centered frog page headings
5. ✅ Video thumbnails now visible when page loads (workaround for Kivy issue #7755)
6. ✅ Mystery page shows all 8 frog options (not just 4)
7. ✅ Added answer selection visual feedback (black border + yellow highlight)
8. ✅ Removed emoji icons that displayed as squares with crosses

---

## Prerequisites

Ensure you have:
- Buildozer installed and configured
- Android SDK and NDK properly set up
- Python 3.7+ with Kivy installed
- All dependencies in `requirements.txt`

---

## Step 1: Clean Previous Builds

Before building the new APK, clean any previous build artifacts:

```bash
cd "d:\WORK\Pyhton Mobile\NiceGUI-20251108T095609Z-1-001\NiceGUI"
buildozer android clean
```

This removes:
- `.buildozer` directory cache
- Old compiled files
- Previous APK builds

---

## Step 2: Verify Changes

Quick verification of modified files:

```bash
# Check if all screen files were updated
dir screens\*.py

# Verify documentation was created
dir *.md
```

**Modified Files:**
- `screens/home_screen.py`
- `screens/app_info_screen.py`
- `screens/frog_detail_screen.py`
- `screens/mystery_screen.py`

**New Documentation:**
- `KIVY_FIXES_SUMMARY.md`
- `BEFORE_AFTER_COMPARISON.md`
- `BUILD_INSTRUCTIONS.md` (this file)

---

## Step 3: Build Debug APK

Build a debug version for testing:

```bash
buildozer android debug
```

**Expected Output:**
```
# Buildozer will:
# - Install/update dependencies
# - Compile Python to bytecode
# - Package assets
# - Create APK
# - Output: bin/frogquizapp-0.1-arm64-v8a-debug.apk
```

**Build Time:** 5-15 minutes (depending on system)

**Common Issues:**

1. **SDK/NDK Error:**
   ```bash
   buildozer android update --sdk
   ```

2. **Permissions Error:**
   ```bash
   # Run as administrator on Windows
   # Or use WSL/Linux
   ```

3. **Memory Error:**
   - Close other applications
   - Increase system swap space

---

## Step 4: Deploy to Device

### Option A: Deploy and Run (USB Debugging)

1. Enable USB debugging on Android device
2. Connect device via USB
3. Run:

```bash
buildozer android deploy run
```

This will:
- Install APK on connected device
- Launch the app automatically

### Option B: Manual Installation

1. Build APK:
   ```bash
   buildozer android debug
   ```

2. Locate APK:
   ```bash
   cd bin
   dir *.apk
   ```

3. Transfer to device:
   - Email to yourself
   - Use Google Drive
   - Use ADB: `adb install frogquizapp-0.1-arm64-v8a-debug.apk`

4. Install on device:
   - Open file manager
   - Tap APK file
   - Allow installation from unknown sources if prompted

---

## Step 5: Test All Features

Use this checklist when testing:

### Home Screen Tests
- [ ] All 10 items visible (instructions + 8 frogs + mystery)
- [ ] Labels fully visible (not cut off)
- [ ] "How spectrograms show sound" label displays correctly
- [ ] All frog names display on 2 lines properly
- [ ] "Mystery Frog" label visible
- [ ] Buttons appear square (not stretched)
- [ ] Buttons maintain square shape on rotation
- [ ] All buttons navigate correctly

### App Info Tests
- [ ] Katie Howard credit visible
- [ ] Exhibition name visible
- [ ] Arthur Rylah Institute credit includes "(DEECA)"
- [ ] Louise Durkin mentioned
- [ ] PASE full name "Python-Audio-Spectrogram-Explorer"
- [ ] Photo credits section visible
- [ ] Zak Atkins credit for Peron's Tree Frog
- [ ] Geoff Heard credit for Pobblebonk and Spotted Marsh Frog
- [ ] Back button works

### Instructions Screen Tests
- [ ] Spectrogram image displays correctly
- [ ] All text visible
- [ ] Back button works

### Frog Detail Page Tests (Test with 2-3 different frogs)
- [ ] Frog name displays (e.g., "Growling Grass Frog")
- [ ] Species name displays in italics (e.g., "Ranoidea raniformis")
- [ ] Both names are centered and close together
- [ ] Video shows first frame immediately (thumbnail visible)
- [ ] Video is paused initially
- [ ] Play button displays correctly
- [ ] Play button is square shaped
- [ ] Clicking play starts video
- [ ] Play button changes to pause icon
- [ ] Video plays with audio
- [ ] Frog photo displays on right
- [ ] Back button is square shaped
- [ ] Back button returns to home

### Mystery Frog Page Tests
- [ ] Title "Mystery Frog Quiz" displays (no emoji)
- [ ] Video shows first frame (thumbnail visible)
- [ ] Video is paused initially
- [ ] Back button is square
- [ ] Play button is square
- [ ] Play button works correctly
- [ ] **8 answer buttons appear** (not 4)
- [ ] Buttons arranged in 4×2 grid
- [ ] All 8 frog names visible on buttons
- [ ] Clicking an answer adds black border
- [ ] Correct answer gets yellow/gold background
- [ ] Other wrong answers fade
- [ ] Result text appears ("CORRECT!" or "Oops!")
- [ ] No emoji display issues (no squares with X)
- [ ] "Try Again?" button appears (no emoji)
- [ ] "Try Again?" button loads new quiz
- [ ] New quiz has different frog

---

## Step 6: Monitor for Errors

### View Live Logs

While app is running on device:

```bash
buildozer android logcat
```

**Look for:**
- Python exceptions
- Video loading errors
- Button sizing issues
- Navigation errors

**Filter for app logs:**
```bash
buildozer android logcat | grep -i "python"
```

### Common Log Messages

**Normal:**
```
Loading video: assets/GGF_resized.mp4
✓ Video file found: assets/GGF_resized.mp4
Video paused at first frame
```

**Issues to Watch:**
```
✗ Video file NOT found: ...
Error loading video: ...
Video playback error: ...
```

---

## Step 7: Release Build (Production)

After testing is complete and all features work:

### Create Release APK

```bash
buildozer android release
```

### Sign the APK

1. Generate keystore (first time only):
   ```bash
   keytool -genkey -v -keystore my-release-key.jks -keyalg RSA -keysize 2048 -validity 10000 -alias my-key-alias
   ```

2. Sign APK:
   ```bash
   jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore my-release-key.jks bin/frogquizapp-0.1-arm64-v8a-release-unsigned.apk my-key-alias
   ```

3. Align APK:
   ```bash
   zipalign -v 4 bin/frogquizapp-0.1-arm64-v8a-release-unsigned.apk bin/frogquizapp-0.1-release.apk
   ```

---

## Troubleshooting

### Issue: Buttons Still Stretching

**Solution:**
```python
# Ensure this code is in the file:
def _update_button_size(self, button, container):
    if container.width > 0 and container.height > 0:
        size = min(container.width, container.height)
        button.size = (size, size)
```

### Issue: Video Black Screen

**Solution:**
1. Check video file exists in `assets/` folder
2. Verify video codec is H.264
3. Check logs for video errors
4. Ensure video file is included in buildozer.spec

### Issue: Mystery Page Only 4 Answers

**Solution:**
Verify in `screens/mystery_screen.py`:
```python
self.answer_grid = GridLayout(cols=4, ...)  # Not cols=2
options = random.sample([...], k=min(7, len(FROGS) - 1))  # Not k=3
```

### Issue: Emojis Show as Squares

**Solution:**
Verify all emoji characters removed from:
- Title: "Mystery Frog Quiz" (not "🐸 Mystery...")
- Button: "Try Again?" (not "🔄 Try...")
- Results: "CORRECT!" (not "✅ Correct!")

### Issue: Labels Cut Off

**Solution:**
Verify in `screens/home_screen.py`:
```python
inst_btn = Button(..., size_hint=(1, 0.85))  # Not (1, 1)
inst_label = Label(..., size_hint=(1, 0.15), valign='top')
```

---

## Performance Optimization

If app is slow on device:

1. **Reduce video quality** (already using `_resized.mp4`):
   ```bash
   ffmpeg -i input.mp4 -vcodec h264 -b:v 1M -s 1280x720 output.mp4
   ```

2. **Enable proguard** in buildozer.spec:
   ```ini
   android.add_compile_options = proguard
   ```

3. **Use release build** (smaller, faster):
   ```bash
   buildozer android release
   ```

---

## Distribution

### Google Play Store

1. Create signed release APK (see Step 7)
2. Go to Google Play Console
3. Create new app
4. Upload APK
5. Fill in store listing
6. Set pricing (free/paid)
7. Submit for review

### Direct Distribution

1. Host APK on website
2. Share download link
3. Users must enable "Unknown Sources" in Android settings

### Email Distribution

1. Attach APK to email (if < 25MB)
2. Or use Google Drive/Dropbox link
3. Send to client/testers

---

## Verification Checklist for Client

Send this checklist with APK:

- [ ] Downloaded APK file
- [ ] Installed on Android device
- [ ] App launches successfully
- [ ] Home page labels not cut off
- [ ] App Info shows photographer credits
- [ ] Buttons are square (not stretched)
- [ ] Frog page headings centered
- [ ] Videos show thumbnails
- [ ] Mystery page has 8 options
- [ ] Answer selection shows black border
- [ ] Correct answer shows yellow background
- [ ] No emoji display issues
- [ ] All navigation works correctly

---

## Contact for Issues

If you encounter issues during build or testing:

1. Check logs: `buildozer android logcat`
2. Verify all files were modified correctly
3. Clean and rebuild: `buildozer android clean && buildozer android debug`
4. Check documentation files for detailed explanations

---

## Final Notes

- All changes match Windows PyQt6 version
- Video thumbnail workaround addresses Kivy issue #7755
- Button aspect ratios dynamically maintained
- Emoji removed for Android compatibility
- All 8 client requirements implemented successfully

**Build Time:** ~10-15 minutes  
**APK Size:** ~30-50MB (with assets)  
**Minimum Android:** 5.0 (API 21)  
**Target Android:** 11+ (API 30+)

---

**Ready to build and deploy! 🚀**
