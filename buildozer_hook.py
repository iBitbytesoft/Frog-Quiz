#!/usr/bin/env python3
"""
Buildozer hook to inject gradle.properties with increased memory settings
This runs during the build process to ensure Gradle has enough memory
"""
import os
import shutil
from pathlib import Path

def hook(ctx):
    """
    Hook called by buildozer during the build process
    """
    print("=" * 60)
    print("BUILDOZER HOOK: Injecting Gradle memory configuration")
    print("=" * 60)
    
    gradle_props_content = """# Gradle Memory Configuration - Injected by Buildozer Hook
org.gradle.jvmargs=-Xmx6g -XX:MaxMetaspaceSize=1024m -XX:+HeapDumpOnOutOfMemoryError -Dfile.encoding=UTF-8
org.gradle.parallel=true
org.gradle.daemon=true
org.gradle.caching=true
org.gradle.configureondemand=true

# Android Configuration
android.useAndroidX=true
android.enableJetifier=true
android.enableR8.fullMode=true
"""
    
    # Find all potential gradle project directories
    buildozer_dir = Path(".buildozer")
    if buildozer_dir.exists():
        # Look for gradle directories
        for gradle_dir in buildozer_dir.rglob("*gradle*"):
            if gradle_dir.is_dir():
                gradle_props_file = gradle_dir.parent / "gradle.properties"
                try:
                    gradle_props_file.write_text(gradle_props_content)
                    print(f"✓ Created gradle.properties in: {gradle_props_file}")
                except Exception as e:
                    print(f"✗ Failed to create in {gradle_props_file}: {e}")
        
        # Look for build.gradle files
        for build_gradle in buildozer_dir.rglob("build.gradle"):
            gradle_props_file = build_gradle.parent / "gradle.properties"
            try:
                gradle_props_file.write_text(gradle_props_content)
                print(f"✓ Created gradle.properties in: {gradle_props_file}")
            except Exception as e:
                print(f"✗ Failed to create in {gradle_props_file}: {e}")
    
    # Also place in root
    root_gradle_props = Path("gradle.properties")
    try:
        root_gradle_props.write_text(gradle_props_content)
        print(f"✓ Created gradle.properties in project root")
    except Exception as e:
        print(f"✗ Failed to create in root: {e}")
    
    print("=" * 60)
    print("BUILDOZER HOOK: Completed")
    print("=" * 60)

# Allow direct execution for testing
if __name__ == "__main__":
    class MockContext:
        pass
    hook(MockContext())
