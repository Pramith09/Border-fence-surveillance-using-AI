# threat_engine/threat_fusion.py

def compute_threat_score(sensor_data, vision_result, nlp_result):
    score = 0

    # Sensor analysis
    if sensor_data['intrusion_detected']:
        score += 3

    # Vision analysis
    if vision_result.get('suspicious', False):
        score += 2

    # NLP analysis
    top_label = nlp_result['labels'][0]
    if top_label == 'terrorism':
        score += 3
    elif top_label in ['violence', 'propaganda']:
        score += 2

    if score >= 6:
        level = "High Threat"
    elif score >= 3:
        level = "Moderate Threat"
    else:
        level = "Low Threat"

    return {
        "threat_score": score,
        "threat_level": level
    }
