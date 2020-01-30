using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DynamicColorChange : MonoBehaviour
{
    public bool colorRandomizer = false; 

    public float colorRed = 4;
    public float colorGreen = 4;
    public float colorBlue = 8;

    private float colorRedMax;
    private float colorGreenMax;
    private float colorBlueMax; 

    // Start is called before the first frame update
    void Start()
    {
        //Setting default variables (before any action by the randomizer)
        colorRedMax = colorRed;
        colorGreenMax = colorGreen;
        colorBlueMax = colorBlue; 
        
    }

    // Update is called once per frame
    void Update()
    {
        //lerpedColor = Color.Lerp(Color.white, Color.red, Mathf.PingPong(Time.time, 1));
        // GetComponent<Renderer>().material.color = new Color(Color.Lerp(Color.white, Color.red, Mathf.PingPong(Time.deltaTime, 1)) );
        GetComponent<Renderer>().material.color = new Color(Mathf.PingPong(Time.time, colorRed), Mathf.PingPong(Time.time, colorGreen), Mathf.PingPong(Time.time, colorBlue));

        if (colorRandomizer == true)
        {
            colorRed = Random.Range(0, colorRedMax);
            colorGreen = Mathf.Lerp(0, colorGreenMax, Time.time);
            colorBlue = Mathf.Clamp(colorBlue, 0, colorBlueMax); 

        }


    }
}
