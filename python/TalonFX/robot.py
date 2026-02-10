import wpilib
from wpilib import *
from phoenix6 import CANBus, controls, hardware

class MyRobot(wpilib.TimedRobot):

    double MOTOR_ID = 1.0
    double SHOULDER_ID = 2.0
    double SHOOTING_POSE = 45.0
    double INTAKE_POSE = 120.0
    double HOLDING__POSE = 90.0
    double SHOOTING_VOLTS = 12.2
    double INTAKE_VOLTS = -9.0
    double HOLDING_VOLTS = 0.5

    def robotInit(self):
        self.controller = XboxController(0)

        self.shooter = hardware.talonfx(MOTOR_ID)
        self.shoulder = hardware.talonfx(SHOULDER_ID)

        cfg = configs.TalonFXConfiguration()
        
        cfg.slot0.k_s = 0.1
        cfg.slot0.k_v = 0.12
        cfg.slot0.k_p = 5.0
        cfg.slot0.k_i = 0
        cfg.slot0.k_d = 0
        cfg.voltage.peak_forward_voltage = 8
        cfg.voltage.peak_reverse_voltage = -8
        self.shooter.configurator.apply(cfg)

        cfgShoulder = configs.TalonFXConfiguration()

        mm = cfgShoulder.motion_magic
        mm.motion_magic_cruise_velocity = 5
        mm.motion_magic_acceleration = 10
        mm.motion_magic_jerk = 100

        slot0 = cfgShoulder.slot0
        slot0.k_s = 0.25
        slot0.k_v = 0.12
        slot0.k_a = 0.01
        slot0.k_p = 60
        slot0.k_i = 0
        slot0.k_d = 0.5
        self.shoulder.configurator.apply(cfgShoulder)

    def teleopPeriodic(self):
        if self.controller.getLeftTrigger() {
            self.shooter.set_control(controls.voltage(SHOOTING_VOLTS))
        } elif self.controller.getRightTrigger() {
            self.shooter.set_control(controls.voltage(INTAKE_VOLTS))
        } else {
            self.shooter.set_control(controls.voltage(HOLDING_VOLTS))
        }

        if self.controller.getLeftBumper() {
            self.shoulder.set_control(controls.MotionMagicVoltage(SHOOTING_POSE))
        } elif self.controller.getRightBumper() {
            self.shoulder.set_control(controls.MotionMagicVoltage(INTAKE_POSE))
        } else {
            self.shoulder.set_control(controls.MotionMagicVoltage(HOLDING__POSE))
        }

if __name__ == "__main__":
    wpilib.run(MyRobot)
