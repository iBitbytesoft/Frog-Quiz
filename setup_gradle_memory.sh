#!/bin/bash
# Script to ensure gradle.properties is in the right place for Buildozer builds

echo "=== Gradle Memory Configuration Script ==="

# Create gradle.properties with maximum memory settings
cat > gradle.properties << EOF
# Gradle Memory Configuration for Android Build
org.gradle.jvmargs=-Xmx6g -XX:MaxMetaspaceSize=1024m -XX:+HeapDumpOnOutOfMemoryError -Dfile.encoding=UTF-8
org.gradle.parallel=true
org.gradle.daemon=true
org.gradle.caching=true
org.gradle.configureondemand=true

# Android Configuration
android.useAndroidX=true
android.enableJetifier=true
android.enableR8.fullMode=true
EOF

echo "Created gradle.properties:"
cat gradle.properties

# Copy to potential Buildozer locations
echo ""
echo "=== Copying gradle.properties to Buildozer directories ==="

# Wait for buildozer to create directories, then copy
while true; do
    if [ -d ".buildozer/android/platform" ]; then
        cp gradle.properties .buildozer/android/platform/ 2>/dev/null || true
        echo "Copied to .buildozer/android/platform/"
    fi
    
    # Look for any gradle project directories
    find .buildozer -type d -name "gradle" 2>/dev/null | while read dir; do
        parent=$(dirname "$dir")
        cp gradle.properties "$parent/" 2>/dev/null || true
        echo "Copied to $parent/"
    done
    
    # Also look for any Android project directories
    find .buildozer -name "build.gradle" 2>/dev/null | while read gradle_file; do
        project_dir=$(dirname "$gradle_file")
        cp gradle.properties "$project_dir/" 2>/dev/null || true
        echo "Copied to $project_dir/"
    done
    
    sleep 2
done &

COPIER_PID=$!
echo "Started gradle.properties copier with PID $COPIER_PID"
echo $COPIER_PID > /tmp/gradle_copier.pid
