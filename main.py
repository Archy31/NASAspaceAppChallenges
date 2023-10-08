
from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFile
from panda3d.core import DirectionalLight
from panda3d.core import TransparencyAttrib
from direct.gui.OnscreenImage import OnscreenImage


loadPrcFile('settings.prc')


class Space(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.loadModels()
        self.setupLights()
        self.setupCamera()
        self.setupSkybox()
        

    def setupCamera(self):
        # self.disableMouse()
        # self.camera.setPos(0, 0, 3)

        crosshairs = OnscreenImage(
            image = 'crosshairs.png',
            pos = (0, 0, 0),
            scale = 0.05,
        )

        crosshairs.setTransparency(TransparencyAttrib.MAlpha)
    

    def setupSkybox(self):
        skybox = loader.loadModel('skybox/skybox.egg')
        skybox.setScale(500)
        skybox.setBin('background', 1)
        skybox.setDepthWrite(0)
        skybox.setLightOff()
        skybox.reparentTo(render)


    def loadModels(self):
        planetary = loader.loadModel("Solar_System_Asset_Pack.glb")
        planetary.reparentTo(render)

    
    def setupLights(self):
        mainLight = DirectionalLight('main light')
        mainLightNodePath = render.attachNewNode(mainLight)
        mainLightNodePath.setHpr(30, -60, 0)

        render.setLight(mainLightNodePath)


Space().run()