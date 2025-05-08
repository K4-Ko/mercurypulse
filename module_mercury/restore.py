import subprocess

def restore_services():
    services = {
        "Fax": "Fax",
        "Spooler": "Print Spooler",
        "WSearch": "Windows Search",
        "RemoteRegistry": "Remote Registry",
        "wisvc": "Windows Insider",
        "seclogon": "Secondary Logon",
        "MapsBroker": "Maps Manager",
        "TabletInputService": "Touch Keyboard",
        "CscService": "Offline Files",
        "WcnSvc": "Windows Connect Now",
        "ALG": "Application Layer Gateway",
        "SCardSvr": "Smart Card",
        "WiaRpc": "Image Acquisition",
        "DiagTrack": "Telemetry",
        "RetailDemo": "Retail Demo",
        "WMPNetworkSvc": "Media Sharing",
        "lfsvc": "Geolocation",
        "PcaSvc": "Compatibility Assistant",
        "EntAppSvc": "Enterprise App Management"
    }

    for service, desc in services.items():
        try:
            # Define o serviço como manual (on-demand) ou automático
            subprocess.run(f'sc config "{service}" start= demand', shell=True)
            subprocess.run(f'sc start "{service}"', shell=True)
        except Exception as e:
            with open('mercurypulse/module_mercury/restore_log.txt', 'a', encoding='utf-8') as log:
                log.write(f"[ERROR] Failed to restore {desc} ({service}): {e}\n")

