import edu.stanford.nlp.simple.*;

public class tdata {
	public static void main(String[] args) { 
		// Create a document. No computation is done yet.
		Document doc = new Document("This memo is on behalf of myself and Lynn Blair. \n" +
		"The following is an update on the status of our effort to resolve/clear past due receivable items currently sitting in the a/r aging report. \n" + 
		"A/R-Imbalances, Transportation, Late Pay charges\n" +
		"The attached report reflects all of the remaining A/R items over 30 days related to imbalance, transportation and late pay charges including any unapplied cash.  Gas Logistics has worked very diligently to ensure the A/R is up to date.  Where there were problems, they recruited the help of Marketing and were very successful in bringing closure to some A/R issues.  The items to be included in the write off package (totaling ($3,486.75)) are designated as such and summed separately on the attached report.  Gas Logistics has provided explanations/resolution plans in the right hand column of the report.  To summarize the report, there is exposure of $1,534,792.  Of that, $1,563,897 is made up of four customer issues (Hutchinson Utilities, IES Industries, MidAmerican Energy and Utilicorp-CCI bankruptcy).  There are currently reserves set up for MidAmerican, $221,429 and Utilicorp, $98.496. \n" + 
		"Beginning immediately Gas Logistics will include an aging report for all outstanding a/r as part of the customer accounts status package.  This package has been and will continue to be distributed to all  account managers monthly. \n" +
		"Gas Logistics has the initial responsibility to collect payments from shippers and will involve the account manager when an issue or collection problem occurs.  However the account manager will also have the responsibility to keep themselves informed as to the status of their shippers accounts.  The reports provided to them in the customer accounts status package will help them do so. \n" +
		"Work orders \n" + 
		"Outstanding work order receivables are being researched and reconciled by Tim Bayles in John Cobb's organization and they plan to resolve these balances independent of the transportation-related effort.  Currently it is our understanding there is approximately $1.2m of outstanding work order receivables with $.6 reserved in December, 2001.  Mike McGowan has offered Laura Lantefield's assistance with getting these resolved. \n" +
		"OBA\'s\n" + 
		"OBA\'s were not originally included as part of our a/r focus however Gas Logistics is already putting the same effort into resolving/clearing any OBA issues.  Currently OBA\'s over $200,000 are included in the customer accounts status package.  Gas Logistics is preparing a report similar to the a/r report for OBA\'s under $200,000.  This report will indicate which OBA\'s are reconciled and which ones need a resolution plan.\n" + 
		"Please let Lynn or I know if you have any further questions.\n"+
		"Dana");
		//for (Sentence sent : doc.sentences()) {  // Will iterate over two sentences
		//	// We're only asking for words -- no need to load any models yet
		//	System.out.println("The second word of the sentence '" + sent + "' is " + sent.word(1));
		//	// When we ask for the lemma, it will load and run the part of speech tagger
		//	System.out.println("The third lemma of the sentence '" + sent + "' is " + sent.lemma(2));
		//	// When we ask for the parse, it will load and run the parser
		//	System.out.println("The parse of the sentence '" + sent + "' is " + sent.parse());
		//	// ...
		//}
		System.out.println("The coreference resolution of the doc is : " + doc.coref());
	}
}


