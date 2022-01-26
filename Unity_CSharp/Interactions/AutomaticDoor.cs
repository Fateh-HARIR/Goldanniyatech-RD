using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AutomaticDoor : MonoBehaviour
{
    public bool openingDoor;
    public bool closingDoor; 

    public float doorTimer;

    public GameObject doorLight1;
    public GameObject doorLight2;
    public GameObject doorLight3; 

    void Start()
    {
        
    }
     

    void Update()
    {
        if (openingDoor is true && doorTimer < 2f)
        {
            this.transform.Translate(Vector3.forward * Time.deltaTime); 
            doorTimer = doorTimer + Time.deltaTime;
            Debug.Log(doorTimer); 
        }

        if (closingDoor is true && doorTimer > 0)
        {
            this.transform.Translate( (Vector3.forward * -1) * Time.deltaTime);
            doorTimer = doorTimer - Time.deltaTime;
        }
    }


    void OnTriggerEnter (Collider other)
    {
        if (other.CompareTag("Player"))
        {
            Debug.Log("Entered");
            closingDoor = false; 
            openingDoor = true;

            doorLight1.GetComponent<Renderer>().material.color = Color.green;
            doorLight2.GetComponent<Renderer>().material.color = Color.green;
            doorLight3.GetComponent<Renderer>().material.color = Color.green; 
        } 

    }

    void OnTriggerExit (Collider other)
    {
        if(other.CompareTag("Player"))
        {
            Debug.Log("Exit");
            openingDoor = false;
            closingDoor = true;

            doorLight1.GetComponent<Renderer>().material.color = Color.red;
            doorLight2.GetComponent<Renderer>().material.color = Color.red;
            doorLight3.GetComponent<Renderer>().material.color = Color.red; 
        }
    }

}






 
