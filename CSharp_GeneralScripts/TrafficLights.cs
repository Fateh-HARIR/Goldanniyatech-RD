using UnityEngine;
using System.Collections;

[AddComponentMenu ("C#/Interactions/Traffic Lights") ] 
public class TrafficLights : MonoBehaviour {
	
public bool MainLightSystem = true ; 
	
public GameObject TrafficLight_Red ; 
public GameObject TrafficLight_Orange ; 
public GameObject TrafficLight_Green ; 
	
public Texture OffLights ; 
public Texture RedLight ;
public Texture OrangeLight ;
public Texture GreenLight ;  
	
	 
void Start () { 
       if  (MainLightSystem == true ) { StartCoroutine(TrafficLight() ); }
		
	   TrafficLight_Green = GameObject.Find ("TrafficLight_Green") ; 
	   TrafficLight_Red = GameObject.Find ("TrafficLight_Red") ; 
	   TrafficLight_Orange = GameObject.Find ("TrafficLight_Orange") ; 
	     }
	
	
IEnumerator TrafficLight () 
	{
		while (true) 
		{
		// Debug.Log ("RedLight") ;
		GetComponent<Renderer>().material.SetTexture ("_MainTex", RedLight) ;
		TrafficLight_Green.GetComponent<Light>().intensity = 0.0f ;
		TrafficLight_Red.GetComponent<Light>().intensity = 3.0f ;
		TrafficLight_Orange.GetComponent<Light>().intensity = 0.0f ;
        yield return new WaitForSeconds(12.0f); 
			
		// Debug.Log ("Green Light");  
		GetComponent<Renderer>().material.SetTexture ("_MainTex", GreenLight) ;
		TrafficLight_Green.GetComponent<Light>().intensity = 3.0f ;
		TrafficLight_Red.GetComponent<Light>().intensity = 0.0f ;  
        yield return new WaitForSeconds(12.0f) ;  
		
		// Debug.Log ("Orange Light"); 
		GetComponent<Renderer>().material.SetTexture ("_MainTex", OrangeLight); 
		TrafficLight_Orange.GetComponent<Light>().intensity = 3.0f ; 
		TrafficLight_Green.GetComponent<Light>().intensity = 0.0f ; 
		yield return new WaitForSeconds (2.0f); 
		
		
		}
 
	}
}
