import cv2
import webbrowser
import time

class QRScanner:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.detected = False
        self.qr_detector = cv2.QRCodeDetector()

    def start(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            data, bbox, _ = self.qr_detector.detectAndDecode(frame)

            if data:
                self.detected = True

                if bbox is not None:
                    bbox = bbox[0].astype(int)

                    # Draw initial boundary
                    cv2.polylines(frame, [bbox], True, (0, 255, 0), 2)

                    x, y = bbox[0]
                    cv2.putText(
                        frame,
                        "QR Detected",
                        (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0, 255, 0),
                        2
                    )

                    cv2.imshow("QR Scanner", frame)
                    cv2.waitKey(100)

                    # ---------- ANIMATION (expanding polygon) ----------
                    for i in range(10):
                        temp = frame.copy()
                        expanded = bbox.copy()
                        expanded[:, 0] -= i
                        expanded[:, 1] -= i
                        cv2.polylines(temp, [expanded], True, (0, 255, 0), 2)
                        cv2.imshow("QR Scanner", temp)
                        cv2.waitKey(40)
                    # --------------------------------------------------

                # Boot up browser
                webbrowser.open(data)

                self.cap.release()
                cv2.destroyAllWindows()
                return data

            cv2.imshow("QR Scanner", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()
        return None
