using System.Collections;
using System.Collections.Generic;
//using System.Link;
using System.Text;
using System.Threading.Tasks; 

using UnityEngine;
using UnityEngine.Networking; 

public class UNETWebRequests : MonoBehaviour
{

    string database_connection = "server=localhost" + "uid=root";

    // Start is called before the first frame update
    void Start()
    {

        UnityWebRequest wr = new UnityWebRequest();
        UnityWebRequest wr2 = new UnityWebRequest("http://www.google.fr"); // target

        StartCoroutine(GetText());

    }

    // Update is called once per frame
    void Update()
    {
        
        
        
    }


    IEnumerator GetText()
    {
        UnityWebRequest www = new UnityWebRequest("http://unity3d.com");
        www.downloadHandler = new DownloadHandlerBuffer();
        yield return www.SendWebRequest(); 

        if (www.isNetworkError || www.isHttpError)
        {
            Debug.Log(www.error);
        }
        else
        {
            //Showing result as text
            Debug.Log(www.downloadHandler);
            //StringBuilder sb = new StringBuilder(); 
            //foreach (System.Collections.Generic.KeyValuePair<string, string> dict in www.GetResponseHeader())
           // {
           //     sb.Append(dict.Key).Append(": \t[").Append(dict.Value).Append("]\n");
            //}

            //Print Header 
            //Debug.Log(sb.ToString());

            //print Body
            Debug.Log(www.downloadHandler.text); 
        }

    }



}
