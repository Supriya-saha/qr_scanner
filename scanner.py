import cv2
import webbrowser
import time
import numpy as np

class QRScanner:
    def __init__(self):  # Initialize the QR code scanner
        self.cap = cv2.VideoCapture(0)
        self.detected = False
        self.qr_detector = cv2.QRCodeDetector()

    def _create_spotlight_effect(self, frame, bbox, alpha=0.5):
        """Create a dimmed frame with spotlight on the QR code"""
        dimmed = frame.copy()
        # Mask for the QR code area
        mask = np.zeros(frame.shape[:2], dtype=np.uint8)
        # Ensure bbox is properly formatted
        bbox_array = np.array([bbox], dtype=np.int32)
        cv2.fillPoly(mask, bbox_array, 255)
        
        dimmed[mask == 0] = cv2.addWeighted(dimmed[mask == 0], 1 - alpha, 
                                            np.zeros_like(dimmed[mask == 0]), alpha, 0)
        return dimmed

    def start(self):  # Start scanning
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            data, bbox, _ = self.qr_detector.detectAndDecode(frame)

            if data:
                self.detected = True

                if bbox is not None:
                    bbox = bbox[0].astype(int)

                    # Spotlight effect
                    for i in range(8):
                        spotlight_frame = self._create_spotlight_effect(frame, bbox, alpha=0.3 + (i * 0.05))
                        
                        # Draw QR outline
                        cv2.polylines(spotlight_frame, [bbox], True, (0, 255, 0), 3)
                        
                        # Add label
                        x, y = bbox[0]
                        cv2.putText(
                            spotlight_frame,
                            "QR Detected",
                            (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.7,
                            (0, 255, 0),
                            2
                        )
                        
                        cv2.imshow("QR Scanner", spotlight_frame)
                        cv2.waitKey(50)

                    # Zoom animation
                    num_frames = 15
                    
                    for frame_idx in range(num_frames + 1):
                        # Calculate interpolation progress (0 to 1)
                        progress = frame_idx / num_frames

                        zoom = 1 + (0.5 * progress)
                        
                        # Get QR code center
                        qr_center_x = int(np.mean(bbox[:, 0]))
                        qr_center_y = int(np.mean(bbox[:, 1]))
                        
                        # Create zoomed frame centered on QR code
                        zoomed_frame = cv2.resize(frame, None, fx=zoom, fy=zoom)
                        zoomed_height, zoomed_width = zoomed_frame.shape[:2]
                        
                        # Calculate crop region to keep QR centered
                        frame_height, frame_width = frame.shape[:2]
                        crop_x = max(0, min(int(qr_center_x * zoom) - frame_width // 2, zoomed_width - frame_width))
                        crop_y = max(0, min(int(qr_center_y * zoom) - frame_height // 2, zoomed_height - frame_height))
                        
                        cropped = zoomed_frame[crop_y:crop_y + frame_height, crop_x:crop_x + frame_width]
                        
                        cv2.imshow("QR Scanner", cropped)
                        cv2.waitKey(40)
                    
                # Boot up browser
                webbrowser.open(data)

                self.cap.release()  # Release the camera
                cv2.destroyAllWindows()
                return data

            cv2.imshow("QR Scanner", frame) # Show the camera
            if cv2.waitKey(1) & 0xFF == ord('q'):  # Quit
                break

        self.cap.release()
        cv2.destroyAllWindows()
        return None
