using UnityEngine;
using System.Collections;

//--> Mail 
using System.Net ; 
using System.Net.Mail ;
using System.Net.Security ; 
using System.Security.Cryptography.X509Certificates ;


public class MailManager : MonoBehaviour {

	// Use this for initialization
	void Start () 
	{
		// ---------------------------------
		// ---> Sending mail 
		MailMessage mail = new MailMessage() ; 

		mail.From = new MailAddress ("test@test.com"); 
		mail.To.Add("test@test.com") ; 
		mail.Subject = "Test"; 
		mail.Body = "<color=blue> test</color>  \t Test \n  Test" ; 
		mail.Priority = MailPriority.Normal ; 

		
		// ---------------------------------
		// ---> Connecting to SMTP Server 
		SmtpClient smtpServer = new SmtpClient("smtp.gmail.com"); 
		smtpServer.Port = 587 ; 
		smtpServer.Credentials = new System.Net.NetworkCredential("test@test.com", "Password") as ICredentialsByHost ;
		smtpServer.EnableSsl = true ; 

		ServicePointManager.ServerCertificateValidationCallback = 
			delegate (object s, X509Certificate certificate, X509Chain chain, SslPolicyErrors sslPolicyErrors)
		{ return true; } ; 

		smtpServer.Send(mail);  
		 
		
		// ---------------------------------
		// ---> Connecting by POP3  



	}
	  


	void Update () 
	{
	
	}
}
