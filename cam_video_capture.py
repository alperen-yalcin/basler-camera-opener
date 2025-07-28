from pypylon import pylon

target_serial = "24068739"

available_cameras = pylon.TlFactory.GetInstance().EnumerateDevices()

camera_found = False
for cam_info in available_cameras:
    if cam_info.GetSerialNumber() == target_serial:
        print(f"Camera found: {target_serial}")
        camera_found = True
        break

if not camera_found:
    print("No camera with specified serial number found.")
