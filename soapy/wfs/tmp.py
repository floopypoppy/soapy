    def frame(self, scrns, phase_correction=None, read=True, iMatFrame=False):
        '''
        Runs one WFS frame

        Runs a single frame of the WFS with a given set of phase screens and
        some optional correction. If elongation is set, will run the phase
        calculating and focal plane making methods multiple times for a few
        different heights of LGS, then sum these onto a ``wfsDetectorPlane``.

        Parameters:
            scrns (list): A list or dict containing the phase screens
            correction (ndarray, optional): The correction term to take from the phase screens before the WFS is run.
            read (bool, optional): Should the WFS be read out? if False, then WFS image is calculated but slopes not calculated. defaults to True.
            iMatFrame (bool, optional): If True, will assume an interaction matrix is being measured. Turns off some AO loop features before running

        Returns:
            ndarray: WFS Measurements
        '''

       #If iMatFrame, turn off unwanted effects


        self.zeroData(detector=read, FP=False)

        self.los.frame(scrns)

        self.uncorrectedPhase = self.los.phase.copy()/self.los.phs2Rad
            
        self.calcFocalPlane()

        if read:
            self.makeDetectorPlane()
            self.calculateSlopes()
            self.zeroData(detector=False)

        return self.slopes