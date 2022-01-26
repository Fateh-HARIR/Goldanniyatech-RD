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
/// The <c>CarEngine</c> subclass can be used for the following types of cars: 
/// Big Truck • Cabriolet • Campervan • Coupe • CUV • Hatchback • Micro • Mini Truck • Minivan • Pickup • Roadster • SEDAN • Supercar • SUV • Truck • Van 
/// </summary> 
/// <remarks>
/// This class is sealed. If you need to tweak it, just do it here. If you want to make another version, write a derived class from the VehicleEngine.
/// Known Limitations: 
/// </remarks>

[System.Serializable] 
public sealed class CarEngine : VehicleEngine
{
    string Debug_UnityEditor = "UNITY EDITOR DEBUG LOG: "

    //[Tooltip("Checking if the player is inside the Vehicle's Collider")]
    // PlayerNearVehicle


    // Unity Methods
    protected override void Awake()
    {
 
    }

    protected override void Start ()
    {

    }
    protected override void FixedUpdate()
    {
        
    }
    protected override void Update()
    {

        if (engineStart is true)
        {
            float vertical = Input.GetAxis("Vertical") * engineSpeed * Time.deltaTime;
            transform.Translate(0, 0, vertical);
        }


        if (Input.GetAxis("Horizontal") > 0 && engineStart is true || Input.GetAxis("Horizontal") < 0 && engineStart is true)
        {
            float horizontal = Input.GetAxis("Horizontal") * engineTurningSpeed * Time.deltaTime;
            transform.Rotate(0, horizontal, 0);
        }

    }

    protected override void LateUpdate()
    {
       
    }


    override public void Drive()
    {


    }



    void OnTriggerEnter(Collider other)
    {
        #if UNITY_EDITOR
        Debug.Log(Debug_UnityEditor + "Collider entered the area");
        #endif
    }
    void OnTriggerStay(Collider other)
    {
        #if UNITY_EDITOR
        Debug.Log(Debug_UnityEditor + "Collider stay in the area");
        #endif 
    }
    void OnTriggerExit(Collider other)
    {
        #if UNITY_EDITOR
        Debug.Log(Debug_UnityEditor + "Collider leave the area");
        #endif 
    }


    /*
    void OnCollisionEnter (Collision collision)
    {
        Debug.Log("Collision!");
        
        Debug.Log(other);
        Debug.Log(other.tag); 

        if (other.gameObject == "Player")
        {
            nearEngine = true;
            Debug.Log(nearEngine);
            vehicleActionText.SetActive(true);
        }
    }
    */


    /*
    void OnTriggerExit (Collider other)
    {
        if (other.gameObject.tag == "Player")
        {
            nearEngine = false;
            Debug.Log(nearEngine);
            vehicleActionText.SetActive(false);
        }
    }
    */





}
