from pyspcbridge.const import ArmMode, DoorMode
ARM_MODE_TO_NAME = {
    ArmMode.UNSET: "disarmed",
    ArmMode.PART_SET_A: "partset_a",
    ArmMode.PART_SET_B: "partset_b",
    ArmMode.FULL_SET: "armed",
    ArmMode.PARTLY_SET_A: "partset_a_partly",
    ArmMode.PARTLY_SET_B: "partset_b_partly",
    ArmMode.PARTLY_FULL_SET: "armed_partly",
}

def arm_mode_to_name(mode):
    return ARM_MODE_TO_NAME.get(mode, "unknown")

DOOR_MODE_TO_NAME = {
    DoorMode.NORMAL: "normal",
    DoorMode.LOCKED: "locked",
    DoorMode.UNLOCKED: "unlocked",
}

def door_mode_to_name(mode):
    return DOOR_MODE_TO_NAME.get(mode, "unknown")
