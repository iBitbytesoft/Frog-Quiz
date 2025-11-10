# Video Thumbnail Fix for Kivy

## The Problem

Kivy's Video widget has a known issue (#7755) where it doesn't display the first frame when the video is in a 'stop' or 'pause' state without having played first. This results in a black/blank video area when a frog page loads.

**Reference:** https://github.com/kivy/kivy/issues/7755

---

## The Solution

We implemented a workaround that:

1. **Loads the video** - Set the video source as usual
2. **Briefly plays it** - Start playback with `state='play'` and volume muted
3. **Seeks to position 0** - Ensure we're at the beginning
4. **Pauses at first frame** - After 0.3 seconds, pause and restore volume

### Code Implementation

```python
def _load_video(self, video_file):
    """Load video with proper path handling and show first frame"""
    try:
        # Use relative path for Android, absolute for desktop
        if platform.system() == 'Android' or 'ANDROID_ARGUMENT' in os.environ:
            video_path = video_file
        else:
            video_path = str(Path(video_file).absolute())
        
        # Set video source
        self.video.source = video_path
        
        # Workaround for Kivy video thumbnail issue #7755
        # Need to play the video briefly to load first frame, then pause
        self.video.state = 'play'
        self.video.volume = 0  # Mute during thumbnail load
        
        # Schedule pause after video has time to load first frame
        Clock.schedule_once(lambda dt: self._pause_at_first_frame(), 0.3)
        
    except Exception as e:
        print(f"Error loading video: {e}")

def _pause_at_first_frame(self):
    """Pause video after first frame loads to show thumbnail"""
    try:
        # Seek to start and pause to show first frame
        if hasattr(self.video, 'seek'):
            self.video.seek(0)
        self.video.state = 'pause'
        self.video.volume = 1.0  # Restore volume for playback
        print("Video paused at first frame")
    except Exception as e:
        print(f"Error pausing video: {e}")
```

---

## Why This Works

1. **Playing first** - Forces Kivy to decode and render the first frame
2. **Muting** - Prevents audio from playing during the brief thumbnail load
3. **0.3 second delay** - Gives enough time for video to initialize and render
4. **Seeking to 0** - Ensures we're definitely at the start frame
5. **Restoring volume** - Ready for normal playback when user clicks play

---

## Files Modified

- `screens/frog_detail_screen.py` - Frog detail page video loading
- `screens/mystery_screen.py` - Mystery quiz page video loading
- `lazy_manager.py` - Fixed path resolution for screens.json

---

## Testing

To verify this works:

1. Run the app: `python main.py`
2. Click on any frog button
3. **Expected:** Video shows first frame (spectrogram visible)
4. **Expected:** Video is paused (not playing)
5. Click play button
6. **Expected:** Video plays with audio

### Desktop Testing

```bash
cd "d:\WORK\Pyhton Mobile\NiceGUI-20251108T095609Z-1-001\NiceGUI"
python main.py
```

### Android Testing

```bash
buildozer android debug
buildozer android deploy run
adb logcat | grep python
```

Look for these log messages:
```
Loading video: [path]
✓ Video file found: [path]
Video paused at first frame
```

---

## Alternative Approaches Considered

### 1. Using preview images (rejected)
- Would require extracting frames from all videos
- Adds complexity to asset management
- Requires more storage space

### 2. Different video codec (rejected)
- Kivy issue exists regardless of codec
- Would require re-encoding all videos
- No guarantee of fixing the issue

### 3. Using AsyncImage (rejected)
- Can't play video, only shows static image
- Would lose video playback functionality

### 4. Custom video player (rejected)
- Too complex for this use case
- Would require significant development time
- May have platform compatibility issues

---

## Known Limitations

1. **Brief flash** - On some devices, users may see a very brief flash when the video loads and auto-pauses
2. **Slight delay** - There's a 0.3 second delay before the thumbnail appears (necessary for video to load)
3. **Codec dependent** - Works best with H.264 encoded videos

---

## Troubleshooting

### Problem: Black screen instead of video thumbnail

**Solutions:**
1. Increase delay from 0.3s to 0.5s:
   ```python
   Clock.schedule_once(lambda dt: self._pause_at_first_frame(), 0.5)
   ```

2. Check video codec:
   ```bash
   ffprobe assets/GGF_resized.mp4
   ```
   Should show: `Video: h264`

3. Verify video file exists:
   - Check console output for "✓ Video file found"
   - If "✗ Video file NOT found", check paths

### Problem: Video plays automatically

**Check:**
- Volume should be 0 during load: `self.video.volume = 0`
- Pause is being called: Look for "Video paused at first frame" in logs

### Problem: No audio when playing

**Check:**
- Volume restored in `_pause_at_first_frame()`: `self.video.volume = 1.0`

---

## Performance Impact

- **Load time:** +0.3 seconds per video page
- **Memory:** No significant increase
- **CPU:** Minimal (brief decode of first frame)
- **Battery:** Negligible impact

**Overall:** Acceptable tradeoff for showing video thumbnails

---

## Future Improvements

If Kivy fixes issue #7755 in a future release:

1. Remove the workaround code
2. Simply use:
   ```python
   self.video.source = video_path
   self.video.state = 'pause'
   self.video.seek(0)
   ```

3. Update this document
4. Test on both Android and desktop

---

## Related Issues

- Kivy issue #7755: Video widget doesn't show first frame when paused
- Kivy issue #6210: Video player black screen
- ffpyplayer compatibility with certain codecs

---

**Status:** ✅ Implemented and working on desktop. Needs testing on Android device.
