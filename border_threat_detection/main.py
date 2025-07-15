from PIL import Image
import os
import json

from data_simulation.sensor_simulator import simulate_sensor_data 
from ai_models.vision_detection import analyze_media
from ai_models.nlp_threat_detection import analyze_text_threat
from threat_engine.threat_fusion import compute_threat_score

# Check if image exists, if not create it
if not os.path.isfile('assets/border_intrusion1.jpg'):
    os.makedirs('assets', exist_ok=True)
    img = Image.new('RGB', (640, 480), color=(73, 109, 137))
    img.save('assets/border_intrusion1.jpg')
    print("Created missing dummy image assets/border_intrusion1.jpg")

def main():
    # Simulate sensor data
    sensor = simulate_sensor_data()

    # Analyze media files (image or video)
    media_files = [
        
        "assets/sample_video1.mp4",
        "assets/border_intrusion1.jpg",
        "assets/threat_text.txt",
        "assets/threat_text.txt1"
    ]
    vision_result = analyze_media(media_files)[0]  # Take first result

    # Read threat text from file
    with open("assets/threat_text.txt", "r") as file:
        threat_text = file.read()

    # Analyze threat from text
    nlp_result = analyze_text_threat(threat_text)

    # Fuse all results and calculate threat score
    threat = compute_threat_score(sensor, vision_result, nlp_result)

    # Print results to console
    print("\n--- THREAT ASSESSMENT ---")
    print("Sensor:", sensor)
    print("Vision:", vision_result)
    print("NLP:", nlp_result['labels'][:2])
    print("Threat Level:", threat)

    # ✅ Save results to JSON for the dashboard
    results = {
        "Sensor": sensor,
        "Vision": vision_result,
        "NLP": nlp_result['labels'][:2],  # Keep only top 2 keywords
        "Threat Level": threat
    }

    output_path = "output/threat_report.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w") as f:
        json.dump(results, f, indent=4)

    print(f"[INFO] Threat report saved to {output_path}")

if __name__ == "__main__":
    main()
