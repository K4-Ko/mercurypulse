import subprocess
import ctypes

def disable_unnecessary_services():
    services = [
        "Fax",
        "Spooler",  # Print Spooler
        "WSearch",  # Windows Search
        "RemoteRegistry",
        "wisvc",  # Windows Insider
        "seclogon",  # Secondary Logon
        "MapsBroker",  # Downloaded Maps Manager
        "TabletInputService",  # Touch Keyboard and Handwriting
        "CscService",  # Offline Files
        "WcnSvc",  # Windows Connect Now
        "ALG",  # Application Layer Gateway
        "SCardSvr",  # Smart Card
        "WiaRpc",  # Windows Image Acquisition
        "DiagTrack",  # Telemetry
        "RetailDemo",
        "WMPNetworkSvc",  # Media Player sharing
        "lfsvc",  # Geolocation
        "PcaSvc",  # Compatibility Assistant
        "EntAppSvc"  # Enterprise App Management
    ]
    try:
        for service in services:
            subprocess.run(f'sc stop "{service}"', shell=True)
            subprocess.run(f'sc config "{service}" start=disabled', shell=True)
    except PermissionError as e:
        print(f"Error disabling service {service}: {e}")
        with open('mercurypulse\\module_mercury\\fps_mode_log.txt','a',encoding = 'UTF-8') as log_file:
            log_file.write(f"Permission denied: {service}\n")

def fps_boost():
    subprocess.run('reg add "HKCU\\Software\\Microsoft\\GameBar" /v AutoGameModeEnabled /t REG_DWORD /d 1 /f', shell=True)
    ctypes.windll.ntdll.NtSetTimerResolution(10000, True, ctypes.byref(ctypes.c_ulong()))
    disable_unnecessary_services()
