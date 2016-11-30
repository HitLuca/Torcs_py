from track_utilities import TrackUtilities

if __name__ == "__main__":
    # TrackUtilities.train_on_all_tracks()
    TrackUtilities().curriculum_learning_on_track(track='a-speedway',
                                         root_dir='curriculum-learning-test-7', initial_speed=290, max_speed=280, validation_lap_number=10, speed_step=10)
    # TrackUtilities.train_on_chosen_tracks(['aalborg', 'a-speedway', 'e-track-6'], [0.5, 0.2, 0], 100000, 'three_tracks')
    #TrackUtilities.test_network('aalborg', 'runs/aalborg_train/aalborg_0.5.h5f')




