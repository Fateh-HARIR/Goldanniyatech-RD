using System.Collections;
using System.Collections.Generic;
using System.Net;
using System.IO; 


using UnityEngine;

public class SystemHttpRequest : MonoBehaviour
{

    private GameObject UnityTextMesh; 

    // Start is called before the first frame update
    void Start()
    {
        //Finding the text mesh (to update result from a website) 
        UnityTextMesh = GameObject.Find("WebTextMesh"); 


        // Use WebClient to retrieve an info from a website. 
        using (WebClient client = new WebClient())
        {
            client.Headers["User-Agent"] =
                "Mozilla/4.0 (Compatible; Windows NT 5.1; MSIE 6.0";

            // Download Data 
            byte[] arr = client.DownloadData("http://www.dotnetperls.com/");

            //Write values 
            Debug.Log("----- WebClient Result ----- ");
            Debug.Log(arr.Length);
            string mySuperString = arr.Length.ToString();
            Debug.Log(mySuperString); 
            UnityTextMesh.GetComponent<TextMesh>().text = mySuperString; 
        }


        

    }

    // Update is called once per frame
    void Update()

    {
        

    }
}
 
