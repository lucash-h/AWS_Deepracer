def reward_function(params):
    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']

    # Handle case where car is off the track
    if not all_wheels_on_track:
        return 1e-3  # Penalize if not all wheels are on track

    # Calculate 5 markers for distance from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.20 * track_width
    marker_3 = 0.30 * track_width
    marker_4 = 0.40 * track_width
    marker_5 = 0.5 * track_width

    # Give higher reward if the car is closer to the center line
    if distance_from_center <= marker_1:
        reward = 3.0
    elif distance_from_center <= marker_2:
        reward = 2.5
    elif distance_from_center <= marker_3:
        reward = 1.5
    elif distance_from_center <= marker_4:
        reward = 1.0
    elif distance_from_center <= marker_5:
        reward = 0.5
    else:
        reward = 1e-3  # Likely crashed or close to being off-track

    # Penalize for low speed or reward for high speed
    if speed < 1:
        reward -= 0.2  # Small penalty for low speeds
    else:
        reward += 0.5  # Small bonus for higher speeds

    return float(reward)
