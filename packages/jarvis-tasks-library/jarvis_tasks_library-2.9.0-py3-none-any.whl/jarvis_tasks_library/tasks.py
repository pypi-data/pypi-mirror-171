class Tasks:

    # Redis constants
    PREFIX = "task"

    # Smart lock
    OPEN_SMART_LOCK = "open-smart-lock"
    CLOSE_SMART_LOCK = "close-smart-lock"

    # Home
    # AC Master
    HOME_TURN_ON_COOLING_MASTER = "turn-on-cooling-master"
    HOME_TURN_ON_HEATING_MASTER = "turn-on-heating-master"
    HOME_TURN_OFF_AC_MASTER = "turn-off-ac-master"
    # AC JF
    HOME_TURN_ON_COOLING_JF = "turn-on-cooling-jf"
    HOME_TURN_ON_HEATING_JF = "turn-on-heating-jf"
    HOME_TURN_OFF_AC_JF = "turn-off-ac-jf"
    # Irrigation
    HOME_TURN_ON_IRRIGATION = "home-turn-on-irrigation"
    HOME_TURN_OFF_IRRIGATION = "home-turn-off-irrigation"
    # Pool Pump
    HOME_TURN_ON_POOL_PUMP = "home-turn-on-pool-pump"
    HOME_TURN_OFF_POOL_PUMP = "home-turn-off-pool-pump"
    # Pool water
    HOME_TURN_ON_POOL_WATER = "home-turn-on-pool-water"
    HOME_TURN_OFF_POOL_WATER = "home-turn-off-pool-water"
    # Bar Pump
    HOME_TURN_ON_BAR_PUMP = "home-turn-on-bar-pump"
    HOME_TURN_OFF_BAR_PUMP = "home-turn-off-bar-pump"
    # Front lights
    HOME_TURN_ON_FRONT_LIGHTS = "home-turn-on-front-lights"
    HOME_TURN_OFF_FRONT_LIGHTS = "home-turn-off-front-lights"
    # Front spotlights
    HOME_TURN_ON_FRONT_SPOT_LIGHTS = "home-turn-on-front-spot-lights"
    HOME_TURN_OFF_FRONT_SPOT_LIGHTS = "home-turn-off-front-spot-lights"
    # Back Main lights
    HOME_TURN_ON_BACK_LIGHTS = "home-turn-on-back-lights"
    HOME_TURN_OFF_BACK_LIGHTS = "home-turn-off-back-lights"
    # Entrance lights
    HOME_TURN_ON_ENTRANCE_LIGHTS = "home-turn-on-entrance-lights"
    HOME_TURN_OFF_ENTRANCE_LIGHTS = "home-turn-off-entrance-lights"
    # Garage lights
    HOME_TURN_ON_GARAGE_LIGHTS = "home-turn-on-garage-lights"
    HOME_TURN_OFF_GARAGE_LIGHTS = "home-turn-off-garage-lights"
    # Christmas lights
    HOME_TURN_ON_CHRISTMAS_LIGHTS = "home-turn-on-christmas-lights"
    HOME_TURN_OFF_CHRISTMAS_LIGHTS = "home-turn-off-christmas-lights"

    # Milencinos

    # Irrigation
    ME_TURN_ON_FRONT_IRRIGATION_V1 = "milencinos-turn-on-front-irrigation-v1"
    ME_TURN_OFF_FRONT_IRRIGATION_V1 = "milencinos-turn-off-front-irrigation-v1"
    ME_TURN_ON_FRONT_IRRIGATION_V2 = "milencinos-turn-on-front-irrigation-v2"
    ME_TURN_OFF_FRONT_IRRIGATION_V2 = "milencinos-turn-off-front-irrigation-v2"
    ME_TURN_ON_FRONT_IRRIGATION_V3 = "milencinos-turn-on-front-irrigation-v3"
    ME_TURN_OFF_FRONT_IRRIGATION_V3 = "milencinos-turn-off-front-irrigation-v3"
    ME_TURN_ON_FRONT_IRRIGATION_V4 = "milencinos-turn-on-front-irrigation-v4"
    ME_TURN_OFF_FRONT_IRRIGATION_V4 = "milencinos-turn-off-front-irrigation-v4"
    ME_TURN_ON_FRONT_IRRIGATION_V5 = "milencinos-turn-on-front-irrigation-v5"
    ME_TURN_OFF_FRONT_IRRIGATION_V5 = "milencinos-turn-off-front-irrigation-v5"
    ME_TURN_ON_FRONT_IRRIGATION_V6 = "milencinos-turn-on-front-irrigation-v6"
    ME_TURN_OFF_FRONT_IRRIGATION_V6 = "milencinos-turn-off-front-irrigation-v6"

    ME_TURN_ON_BACK_IRRIGATION_V1 = "milencinos-turn-on-back-irrigation-v1"
    ME_TURN_OFF_BACK_IRRIGATION_V1 = "milencinos-turn-off-back-irrigation-v1"
    ME_TURN_ON_BACK_IRRIGATION_V2 = "milencinos-turn-on-back-irrigation-v2"
    ME_TURN_OFF_BACK_IRRIGATION_V2 = "milencinos-turn-off-back-irrigation-v2"
    ME_TURN_ON_BACK_IRRIGATION_V3 = "milencinos-turn-on-back-irrigation-v3"
    ME_TURN_OFF_BACK_IRRIGATION_V3 = "milencinos-turn-off-back-irrigation-v3"
    ME_TURN_ON_BACK_IRRIGATION_V4 = "milencinos-turn-on-back-irrigation-v4"
    ME_TURN_OFF_BACK_IRRIGATION_V4 = "milencinos-turn-off-back-irrigation-v4"
    ME_TURN_ON_BACK_IRRIGATION_V5 = "milencinos-turn-on-back-irrigation-v5"
    ME_TURN_OFF_BACK_IRRIGATION_V5 = "milencinos-turn-off-back-irrigation-v5"
    ME_TURN_ON_BACK_IRRIGATION_V6 = "milencinos-turn-on-back-irrigation-v6"
    ME_TURN_OFF_BACK_IRRIGATION_V6 = "milencinos-turn-off-back-irrigation-v6"

    # Maps the endpoint to the task name.
    ENDPOINT_TASK_MAP = {
        # Home
        # AC Master
        "/home/ac/master?state=cooling": HOME_TURN_ON_COOLING_MASTER,
        "/home/ac/master?state=heating": HOME_TURN_ON_HEATING_MASTER,
        "/home/ac/master?state=off": HOME_TURN_OFF_AC_MASTER,
        # AC JF
        "/home/jf/master?state=cooling": HOME_TURN_ON_COOLING_JF,
        "/home/jf/master?state=heating": HOME_TURN_ON_HEATING_JF,
        "/home/jf/master?state=off": HOME_TURN_OFF_AC_JF,
        # Irrigation
        "/home/irrigation?state=on": HOME_TURN_ON_IRRIGATION,
        "/home/irrigation?state=off": HOME_TURN_OFF_IRRIGATION,
        # Pool Pump
        "/home/poolPump?state=on": HOME_TURN_ON_POOL_PUMP,
        "/home/poolPump?state=off": HOME_TURN_OFF_POOL_PUMP,
        # Pool Pump
        "/home/poolWater?state=on": HOME_TURN_ON_POOL_WATER,
        "/home/poolWater?state=off": HOME_TURN_OFF_POOL_WATER,
        # Bar Pump
        "/home/barPump?state=on": HOME_TURN_ON_BAR_PUMP,
        "/home/barPump?state=off": HOME_TURN_OFF_BAR_PUMP,
        # Front Lights
        "/home/frontLights?state=on": HOME_TURN_ON_FRONT_LIGHTS,
        "/home/frontLights?state=off": HOME_TURN_OFF_FRONT_LIGHTS,
        # Front Spotlights
        "/home/frontSpotLights?state=on": HOME_TURN_ON_FRONT_SPOT_LIGHTS,
        "/home/frontSpotLights?state=off": HOME_TURN_OFF_FRONT_SPOT_LIGHTS,
        # Backlights
        "/home/backLights?state=on": HOME_TURN_ON_BACK_LIGHTS,
        "/home/backLights?state=off": HOME_TURN_OFF_BACK_LIGHTS,
        # Entrance Lights
        "/home/entranceLights?state=on": HOME_TURN_ON_ENTRANCE_LIGHTS,
        "/home/entranceLights?state=off": HOME_TURN_OFF_ENTRANCE_LIGHTS,
        # Garage Lights
        "/home/garageLights?state=on": HOME_TURN_ON_GARAGE_LIGHTS,
        "/home/garageLights?state=off": HOME_TURN_OFF_GARAGE_LIGHTS,
        # Christmas Lights
        "/home/christmasLights?state=on": HOME_TURN_ON_CHRISTMAS_LIGHTS,
        "/home/christmasLights?state=off": HOME_TURN_OFF_CHRISTMAS_LIGHTS,
        # Milencinos
        # Irrigation
        "/milencinos/irrigation/front/v1?state=on": ME_TURN_ON_FRONT_IRRIGATION_V1,
        "/milencinos/irrigation/front/v1?state=off": ME_TURN_OFF_FRONT_IRRIGATION_V1,
        "/milencinos/irrigation/front/v2?state=on": ME_TURN_ON_FRONT_IRRIGATION_V2,
        "/milencinos/irrigation/front/v2?state=off": ME_TURN_OFF_FRONT_IRRIGATION_V2,
        "/milencinos/irrigation/front/v3?state=on": ME_TURN_ON_FRONT_IRRIGATION_V3,
        "/milencinos/irrigation/front/v3?state=off": ME_TURN_OFF_FRONT_IRRIGATION_V3,
        "/milencinos/irrigation/front/v4?state=on": ME_TURN_ON_FRONT_IRRIGATION_V4,
        "/milencinos/irrigation/front/v4?state=off": ME_TURN_OFF_FRONT_IRRIGATION_V4,
        "/milencinos/irrigation/front/v5?state=on": ME_TURN_ON_FRONT_IRRIGATION_V5,
        "/milencinos/irrigation/front/v5?state=off": ME_TURN_OFF_FRONT_IRRIGATION_V5,
        "/milencinos/irrigation/front/v6?state=on": ME_TURN_ON_FRONT_IRRIGATION_V6,
        "/milencinos/irrigation/front/v6?state=off": ME_TURN_OFF_FRONT_IRRIGATION_V6,
        "/milencinos/irrigation/back/v1?state=on": ME_TURN_ON_BACK_IRRIGATION_V1,
        "/milencinos/irrigation/back/v1?state=off": ME_TURN_OFF_BACK_IRRIGATION_V1,
        "/milencinos/irrigation/back/v2?state=on": ME_TURN_ON_BACK_IRRIGATION_V2,
        "/milencinos/irrigation/back/v2?state=off": ME_TURN_OFF_BACK_IRRIGATION_V2,
        "/milencinos/irrigation/back/v3?state=on": ME_TURN_ON_BACK_IRRIGATION_V3,
        "/milencinos/irrigation/back/v3?state=off": ME_TURN_OFF_BACK_IRRIGATION_V3,
        "/milencinos/irrigation/back/v4?state=on": ME_TURN_ON_BACK_IRRIGATION_V4,
        "/milencinos/irrigation/back/v4?state=off": ME_TURN_OFF_BACK_IRRIGATION_V4,
        "/milencinos/irrigation/back/v5?state=on": ME_TURN_ON_BACK_IRRIGATION_V5,
        "/milencinos/irrigation/back/v5?state=off": ME_TURN_OFF_BACK_IRRIGATION_V5,
        "/milencinos/irrigation/back/v6?state=on": ME_TURN_ON_BACK_IRRIGATION_V6,
        "/milencinos/irrigation/back/v6?state=off": ME_TURN_OFF_BACK_IRRIGATION_V6,
    }

    # Maps the task to the endpoint that task executes.
    TASK_MAP = {
        # Smart lock
        OPEN_SMART_LOCK: "smartLock?state=open",
        CLOSE_SMART_LOCK: "smartLock?state=closed",
        # Home
        # AC Master
        HOME_TURN_ON_COOLING_MASTER: "ac/master?state=cooling",
        HOME_TURN_ON_HEATING_MASTER: "ac/master?state=heating",
        HOME_TURN_OFF_AC_MASTER: "ac/master?state=off",
        # AC JF
        HOME_TURN_ON_COOLING_JF: "ac/jf?state=cooling",
        HOME_TURN_ON_HEATING_JF: "ac/jf?state=heating",
        HOME_TURN_OFF_AC_JF: "ac/jf?state=off",
        # Irrigation
        HOME_TURN_ON_IRRIGATION: "home/irrigation?state=on",
        HOME_TURN_OFF_IRRIGATION: "home/irrigation?state=off",
        # Pool Pump
        HOME_TURN_ON_POOL_PUMP: "home/poolPump?state=on",
        HOME_TURN_OFF_POOL_PUMP: "home/poolPump?state=off",
        # Pool water
        HOME_TURN_ON_POOL_WATER: "home/poolWater?state=on",
        HOME_TURN_OFF_POOL_WATER: "home/poolWater?state=off",
        # Bar Pump
        HOME_TURN_ON_BAR_PUMP: "home/barPump?state=on",
        HOME_TURN_OFF_BAR_PUMP: "home/barPump?state=off",
        # Front lights
        HOME_TURN_ON_FRONT_LIGHTS: "home/frontLights?state=on",
        HOME_TURN_OFF_FRONT_LIGHTS: "home/frontLights?state=off",
        # Front spotlights
        HOME_TURN_ON_FRONT_SPOT_LIGHTS: "home/frontSpotLights?state=on",
        HOME_TURN_OFF_FRONT_SPOT_LIGHTS: "home/frontSpotLights?state=off",
        # Back Main lights
        HOME_TURN_ON_BACK_LIGHTS: "home/backLights?state=on",
        HOME_TURN_OFF_BACK_LIGHTS: "home/backLights?state=off",
        # Entrance lights
        HOME_TURN_ON_ENTRANCE_LIGHTS: "home/entranceLights?state=on",
        HOME_TURN_OFF_ENTRANCE_LIGHTS: "home/entranceLights?state=off",
        # Garage lights
        HOME_TURN_ON_GARAGE_LIGHTS: "home/garageLights?state=on",
        HOME_TURN_OFF_GARAGE_LIGHTS: "home/garageLights?state=off",
        # Christmas lights
        HOME_TURN_ON_CHRISTMAS_LIGHTS: "home/christmasLights?state=on",
        HOME_TURN_OFF_CHRISTMAS_LIGHTS: "home/christmasLights?state=off",
        # Milencinos
        # Irrigation
        ME_TURN_ON_FRONT_IRRIGATION_V1: "milencinos/irrigation/front/v1?state=on",
        ME_TURN_OFF_FRONT_IRRIGATION_V1: "milencinos/irrigation/front/v1?state=off",
        ME_TURN_ON_FRONT_IRRIGATION_V2: "milencinos/irrigation/front/v2?state=on",
        ME_TURN_OFF_FRONT_IRRIGATION_V2: "milencinos/irrigation/front/v2?state=off",
        ME_TURN_ON_FRONT_IRRIGATION_V3: "milencinos/irrigation/front/v3?state=on",
        ME_TURN_OFF_FRONT_IRRIGATION_V3: "milencinos/irrigation/front/v3?state=off",
        ME_TURN_ON_FRONT_IRRIGATION_V4: "milencinos/irrigation/front/v4?state=on",
        ME_TURN_OFF_FRONT_IRRIGATION_V4: "milencinos/irrigation/front/v4?state=off",
        ME_TURN_ON_FRONT_IRRIGATION_V5: "milencinos/irrigation/front/v5?state=on",
        ME_TURN_OFF_FRONT_IRRIGATION_V5: "milencinos/irrigation/front/v5?state=off",
        ME_TURN_ON_FRONT_IRRIGATION_V6: "milencinos/irrigation/front/v6?state=on",
        ME_TURN_OFF_FRONT_IRRIGATION_V6: "milencinos/irrigation/front/v6?state=off",
        ME_TURN_ON_BACK_IRRIGATION_V1: "milencinos/irrigation/back/v1?state=on",
        ME_TURN_OFF_BACK_IRRIGATION_V1: "milencinos/irrigation/back/v1?state=off",
        ME_TURN_ON_BACK_IRRIGATION_V2: "milencinos/irrigation/back/v2?state=on",
        ME_TURN_OFF_BACK_IRRIGATION_V2: "milencinos/irrigation/back/v2?state=off",
        ME_TURN_ON_BACK_IRRIGATION_V3: "milencinos/irrigation/back/v3?state=on",
        ME_TURN_OFF_BACK_IRRIGATION_V3: "milencinos/irrigation/back/v3?state=off",
        ME_TURN_ON_BACK_IRRIGATION_V4: "milencinos/irrigation/back/v4?state=on",
        ME_TURN_OFF_BACK_IRRIGATION_V4: "milencinos/irrigation/back/v4?state=off",
        ME_TURN_ON_BACK_IRRIGATION_V5: "milencinos/irrigation/back/v5?state=on",
        ME_TURN_OFF_BACK_IRRIGATION_V5: "milencinos/irrigation/back/v5?state=off",
        ME_TURN_ON_BACK_IRRIGATION_V6: "milencinos/irrigation/back/v6?state=on",
        ME_TURN_OFF_BACK_IRRIGATION_V6: "milencinos/irrigation/back/v6?state=off",
    }

    # Maps the tasks to their counter tasks
    COUNTER_TASK_MAP = {
        # Smart lock
        OPEN_SMART_LOCK: CLOSE_SMART_LOCK,
        # Home
        # AC Master
        HOME_TURN_ON_COOLING_MASTER: HOME_TURN_OFF_AC_MASTER,
        HOME_TURN_ON_HEATING_MASTER: HOME_TURN_OFF_AC_MASTER,
        # AC JF
        HOME_TURN_ON_COOLING_JF: HOME_TURN_OFF_AC_JF,
        HOME_TURN_ON_HEATING_JF: HOME_TURN_OFF_AC_JF,
        # Irrigation
        HOME_TURN_ON_IRRIGATION: HOME_TURN_OFF_IRRIGATION,
        # Pool water
        HOME_TURN_ON_POOL_WATER: HOME_TURN_OFF_POOL_WATER,
        # Pool Pump
        HOME_TURN_ON_POOL_PUMP: HOME_TURN_OFF_POOL_PUMP,
        # Bar Pump
        HOME_TURN_ON_BAR_PUMP: HOME_TURN_OFF_BAR_PUMP,
        # Front lights
        HOME_TURN_ON_FRONT_LIGHTS: HOME_TURN_OFF_FRONT_LIGHTS,
        # Front spotlights
        HOME_TURN_ON_FRONT_SPOT_LIGHTS: HOME_TURN_OFF_FRONT_SPOT_LIGHTS,
        # Back Main lights
        HOME_TURN_ON_BACK_LIGHTS: HOME_TURN_OFF_BACK_LIGHTS,
        # Entrance lights
        HOME_TURN_ON_ENTRANCE_LIGHTS: HOME_TURN_OFF_ENTRANCE_LIGHTS,
        # Garage lights
        HOME_TURN_ON_GARAGE_LIGHTS: HOME_TURN_OFF_GARAGE_LIGHTS,
        # Christmas lights
        HOME_TURN_ON_CHRISTMAS_LIGHTS: HOME_TURN_OFF_CHRISTMAS_LIGHTS,
        # Milencinos
        # Irrigation
        ME_TURN_ON_FRONT_IRRIGATION_V1: ME_TURN_OFF_FRONT_IRRIGATION_V1,
        ME_TURN_ON_FRONT_IRRIGATION_V2: ME_TURN_OFF_FRONT_IRRIGATION_V2,
        ME_TURN_ON_FRONT_IRRIGATION_V3: ME_TURN_OFF_FRONT_IRRIGATION_V3,
        ME_TURN_ON_FRONT_IRRIGATION_V4: ME_TURN_OFF_FRONT_IRRIGATION_V4,
        ME_TURN_ON_FRONT_IRRIGATION_V5: ME_TURN_OFF_FRONT_IRRIGATION_V5,
        ME_TURN_ON_FRONT_IRRIGATION_V6: ME_TURN_OFF_FRONT_IRRIGATION_V6,
        ME_TURN_ON_BACK_IRRIGATION_V1: ME_TURN_OFF_BACK_IRRIGATION_V1,
        ME_TURN_ON_BACK_IRRIGATION_V2: ME_TURN_OFF_BACK_IRRIGATION_V2,
        ME_TURN_ON_BACK_IRRIGATION_V3: ME_TURN_OFF_BACK_IRRIGATION_V3,
        ME_TURN_ON_BACK_IRRIGATION_V4: ME_TURN_OFF_BACK_IRRIGATION_V4,
        ME_TURN_ON_BACK_IRRIGATION_V5: ME_TURN_OFF_BACK_IRRIGATION_V5,
        ME_TURN_ON_BACK_IRRIGATION_V6: ME_TURN_OFF_BACK_IRRIGATION_V6,
    }
