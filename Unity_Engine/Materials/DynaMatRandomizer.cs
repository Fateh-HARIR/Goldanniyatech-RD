/* * * * * * * * * * * * * * * * * * * * * * * * 
 *           UNITY LABORATORY PROJECT          *
 *                                             *
 * Author: Yoann AMAR ASSOULINE                * 
 * Script: Dynamic Material Randomizer         *
 *                                             *
 * * * * * * * * * * * * * * * * * * * * * * * */
 
using System; 
using System.Collections;
using System.Collections.Generic;

using UnityEditor; 
using UnityEngine;

/// <summary>
/// The Dynamic Material Randomizer base class can change in real-time a material color. 
/// It's currently limited to one material. 
/// </summary>
public class DynaMatRandomizer : MonoBehaviour
{
    // Serialized Variables
    [SerializeField] 
    protected bool RandomizeColor = true;

    protected enum RandomizeMethod
    {
        Lerp, 
        Undefined
    }
    [SerializeField]
    protected  RandomizeMethod randomizeMethod;

    [SerializeField]
    IDictionary<int, string> randomizeDictionary = new Dictionary<int, string>()
    {
        {1, "Lerp" }
    };

    [SerializeField]
    protected float RandomizeTime = 1.0F; 

    [SerializeField] 
    protected Color FirstColor;

    [SerializeField]
    protected Color SecondColor; 

    // Hidden variables (from the Unity Inspector window)
    protected Material ObjectMaterial; 

    // Start is called before the first frame update
    void Start()
    {
        Debug.Log("RandomizeColor enabled");

        ObjectMaterial = GetComponent<Renderer>().material;
       
        ObjectMaterial.SetColor("_Color", FirstColor); 

    }

    // Update is called once per frame
    void Update()
    {
        if (RandomizeColor == true)
        {  
            ObjectMaterial.color = Color.Lerp(FirstColor, SecondColor, Mathf.PingPong(Time.time, 1));
           
        }
        
    }
}


/// <summary>
///  The DynaMatRandomizerEditor class is dynamically changing variables in the inspector when changing the Randomizer Method. 
/// </summary> 
[CustomEditor(typeof(DynaMatRandomizer)), CanEditMultipleObjects]
public class DynaMatRandomizerEditor : Editor
{

    private void OnEnable()
    {
        
    }
}
