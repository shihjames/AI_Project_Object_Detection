import cv2
import sys
import logging


def to_frames(video_file, max_frame=-1):
	out = []
	cap = cv2.VideoCapture(video_file)
	count = 0
	n_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
	frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
	print("Number of frame {}, fps {}".format(n_frame, frame_rate))
	while count < max_frame or max_frame == -1:
		# Get frame
		ret, frame = cap.read()
		if not ret:
			break
		# Pass frame through yolo detector 
		out.append(frame)
		count += 1
	print("Read {} frames".format(count))
	return out


def modify_frame(frames):
	out_frames = []
	for frame in frames:
		# Crop image to 1:1
		min_len = min(frame.shape[0], frame.shape[1])
		frame = frame[:min_len, :min_len]
		# Resize frame 
		frame = cv2.resize(frame, (344, 344)) 
		# TODO: pass through yolo and add bounding boxes 

		out_frames.append(frame)
	return out_frames


def to_video(frames, name, frame_rate=30):
	fourcc = cv2.VideoWriter_fourcc(*'mp4v')
	# out = cv2.VideoWriter(name, cv2.CAP_OPENCV_MJPEG, fourcc, 20.0, (344, 344))
	out = cv2.VideoWriter(name, fourcc, frame_rate, (344, 344))
	for f in frames:
		out.write(f)
	out.release()
	return out


def main(argv):
	video_file = argv[1]
	out_name = video_file.split(".")[0] + "_out" + ".mp4"
	print("Processing input vid file: {}, Outputing to {}".format(video_file, out_name))
	frames = to_frames(video_file, 300)
	frames = modify_frame(frames)
	out_video = to_video(frames, out_name, 10)


if __name__ == "__main__":
	main(sys.argv)
