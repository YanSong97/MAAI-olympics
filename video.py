import imageio
import os
import numpy as np
import cv2
import pygame

from pathlib import Path
import datetime


class VideoRecorder(object):
    def __init__(self, dir_name, fps=30):
        self.dir_name = dir_name
        # self.env = env
        self.fps = fps
        # width = self.env.env_core.view_setting["width"]
        # height = self.env.env_core.view_setting["height"]
        # edge = self.env.env_core.view_setting["edge"]
        # self.WIN_SIZE = width + 2*edge, height + 2*edge
        # file_path = dir_name + ".mp4v"#导出路径
        # fourcc = cv2.VideoWriter_fourcc('I','4','2','0')#不同视频编码对应不同视频格式（例：'I','4','2','0' 对应avi格式）
        # self.video = cv2.VideoWriter(file_path, fourcc, fps, self.WIN_SIZE)
        self.frames = []

    def init(self):
        self.frames = []

    def record(self, viewer):

        # frame = env.render()

        view = pygame.surfarray.array3d(viewer.background)
        frame = view.transpose([1, 0, 2])
        frame = cv2.resize(frame, (640, 640))


        img = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)

        # self.video.write(img)        #把图片写进视频
        # if CMG.step == len(CMG.gameAnswer)+1: #结束时：释放video，视频就做好了
        #     CMG.video.release() #释放
        self.frames.append(img)

    def save(self):

        time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        base_path = self.dir_name
        save_path = os.path.join(base_path, "olympicsrunning-video: {}.mp4".format(time))
        if os.path.exists(save_path):
            raise FileExistsError


        imageio.mimsave(save_path, self.frames, fps=self.fps)
        # self.video.release() #释放
