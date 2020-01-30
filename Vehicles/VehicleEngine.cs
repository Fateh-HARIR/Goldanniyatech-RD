
/* * * * * * * * * * * * * * * * * * * * * * * * 
 *           UNITY LABORATORY PROJECT          *
 *                                             *
 * Author: Yoann AMAR ASSOULINE                *
 *                                             *
 * * * * * * * * * * * * * * * * * * * * * * * */

 // How to use it: 
 // 
 // C# Concepts used: Multilevel Inheritance 

// DotNet CORE 
using System.Collections;
using System.Collections.Generic;

//
using UnityEngine;


// Base class VehicleEngine will never be used directly in the game. 
public class VehicleEngine : MonoBehaviour
{   
    
    // Booleans for the vehicle's engine
    [Tooltip("Checking if the player is inside the vehicle's box collider")]
    public bool nearEngine = false;
    public bool engineStart = false;
    public bool engineSpeedMax = false;
    public bool engineReverseMax = false;
    public bool engineBroken = false;

    //Variables for the vehicle's parameters
    public int engineGear = 0;
    public int engineSpeed = 0;
    public int engineTurningSpeed = 0;

    // Variables for GameObjects
    public GameObject vehicleActionText; 

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
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

    void LateUpdate()
    {

    }


    void OnTriggerEnter(Collider other)
    {
        Debug.Log("Collider entered the area"); 
    }
    void OnTriggerStay(Collider other)
    {
        Debug.Log("Collider stayed the area"); 
    }
    void OnTriggerExit(Collider other)
    {
        Debug.Log("Collider leaved the area"); 
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





//
public class MotorEngine : VehicleEngine
{

}
public class RailedEngine : VehicleEngine
{

}


// The CarEngine sub class is covering these types of cars: 
// Big Truck • Cabriolet • Campervan • Coupe • CUV • Hatchback • Micro • Mini Truck • Minivan • Pickup • Roadster • SEDAN • Supercar • SUV • Truck • Van 
public class Car : MotorEngine
{

}



