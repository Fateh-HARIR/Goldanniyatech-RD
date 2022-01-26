/* * * * * * * * * * * * * * * * * * * * * * * * * * *
 *                .------------------.               *
 *                | .--------------. |               *
 *                | |  ____  ____  | |               * 
 *                | | |_  _||_  _| | |               *
 *                | |   \ \  / /   | |               *
 *                | |    \ \/ /    | |               * 
 *                | |    _|  |_    | |               * 
 *                | |   |______|   | |               *
 *                | |              | |               *
 *                | '--------------' |               *
 *                '------------------'               * 
 *                                                   *
 *              UNITY LABORATORY PROJECT             *
 *                                                   *
 * Author: Yoann AMAR ASSOULINE                      * 
 * Language: C#                                      * 
 * Game Engine: Unity                                *
 *                                                   *
 * * * * * * * * * * * * * * * * * * * * * * * * * * */

using System.Collections;
using System.Collections.Generic;

using UnityEngine;

/// <summary>
///  The abstract base class <c>VehicleEngine</c> contains various features to define a template for a large variety of vehicles.  
///  Each derived class can be used directly and some parameters tweaked from the Unity inspector Window. 
///  Caution: This is using advanced concepts (polymorphism, inheritance, encapsulation, abstract classes...). If you're not familiar with these topics, please refer to the "VehicleSimpleEngine" script and adapt it to any kind of vehicle. 
/// </summary>  
/// <remarks>
/// Known Limitations: 
/// -> Can handle only one material (to change its properties)
/// </remarks>


abstract public class VehicleEngine : MonoBehaviour
{ 
    /// <summary>
    /// Properties
    /// </summary>

    // Automatic properties for the Vehicle's interaction parameters
    public abstract bool PlayerNearVehicle { get; set;  }
    public abstract bool EngineTurnedOn { get; set;  }
    public abstract bool EngineBroken { get; set;  }

    public abstract int EngineGear { get; set;  }
    public abstract int EngineSpeed { get; set;  }
    public abstract int EngineTurningSpeed { get; set; }

    public abstract bool VehicleLocked { get; set;  }
    public abstract bool SeatDriverDoorLocked { get; set; }
    public abstract bool[] SeatPassengerDoorLocked { get; set;  }
    public abstract int SeatNumber { get; set;  }

    public abstract string VehicleName { get; set; }
    public abstract string VehicleCategory { get; set; }
    public abstract string VehicleDescription { get; set;  }
    public abstract string Transmission { get; set; }

    // Automatic properties for the Vehicle's main characteristics  
    public abstract GameObject VehicleMainModel { get; set;  }
    public abstract Material VehicleMat { get; set;  } 



    // Automatic properties for Debug Purpose 
    public abstract GameObject VehicleDebugText { get; set;  }

    /// <summary>
    /// Methods 
    /// </summary>

    // Abstract Methods0
    protected virtual void Awake() { }
    protected virtual void Start() { }
    protected virtual void FixedUpdate() { }
    protected virtual void Update() { }
    protected virtual void LateUpdate() { }

    public virtual void StartEngine() { }

    public virtual void Drive () { }
    protected virtual void Horn () { }

    public virtual void OpenDriverDoor () { }
    public virtual void OpenPassengerDoor () { }


}


 
