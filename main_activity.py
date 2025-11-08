#from jnius import autoclass
#from android.runnable import run_on_ui_thread

#@run_on_ui_thread
#def start_webview():
#    PythonActivity = autoclass('org.kivy.android.PythonActivity')
 #   WebView = autoclass('android.webkit.WebView')
  #  WebViewClient = autoclass('android.webkit.WebViewClient')
   # LayoutParams = autoclass('android.widget.FrameLayout$LayoutParams')

#    activity = PythonActivity.mActivity
 #   webview = WebView(activity)
  #  webview.getSettings().setJavaScriptEnabled(True)
   # webview.setWebViewClient(WebViewClient())

    # Load your local server (NiceGUI)
#    webview.loadUrl('http://127.0.0.1:8080')

 #   activity.setContentView(webview, LayoutParams(-1, -1))


# main_activity.py
import platform

if platform.system() == 'Android':
    from jnius import autoclass
    try:
        from android.runnable import run_on_ui_thread
    except ImportError:
        # fallback if running outside P4A environment
        def run_on_ui_thread(func):
            return func

def start_webview():
    if platform.system() != 'Android':
        return

    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    WebView = autoclass('android.webkit.WebView')
    WebViewClient = autoclass('android.webkit.WebViewClient')
    LayoutParams = autoclass('android.widget.FrameLayout$LayoutParams')

    activity = PythonActivity.mActivity
    webview = WebView(activity)
    webview.getSettings().setJavaScriptEnabled(True)
    webview.setWebViewClient(WebViewClient())
    webview.loadUrl('http://127.0.0.1:8080')
    activity.setContentView(webview, LayoutParams(-1, -1))
