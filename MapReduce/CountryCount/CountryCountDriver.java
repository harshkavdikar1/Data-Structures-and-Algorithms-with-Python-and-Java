package CountryCount;

import java.io.IOException;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.FileInputFormat;
import org.apache.hadoop.mapred.FileOutputFormat;
import org.apache.hadoop.mapred.JobClient;
import org.apache.hadoop.mapred.JobConf;
import org.apache.hadoop.mapred.TextInputFormat;
import org.apache.hadoop.mapred.TextOutputFormat;

public class CountryCountDriver {
	public static void main(String args[]) {
		JobClient jobClient = new JobClient();
		
		// Create a configuration object for the job
		JobConf jobConf = new JobConf(CountryCountDriver.class);
		
		//Set a name
		jobConf.setJobName("Sales");
		
		// Specify data type of output key and value
		jobConf.setOutputKeyClass(Text.class);
		jobConf.setOutputValueClass(IntWritable.class);
		
		// Specify names of Mapper and Reducer Class
		jobConf.setMapperClass(CountryCountMapper.class);
		jobConf.setReducerClass(CountryCountReducer.class);
		
		// Specify formats of the data type of Input and output
		jobConf.setInputFormat(TextInputFormat.class);
		jobConf.setOutputFormat(TextOutputFormat.class);
		
		// Set input and output directories using command line arguments, 
        //arg[0] = name of input directory on HDFS, and arg[1] =  name of output directory to be created to store the output file.
		FileInputFormat.setInputPaths(jobConf, new Path(args[0]));
		FileOutputFormat.setOutputPath(jobConf, new Path(args[1]));
		
		jobClient.setConf(jobConf);
		
		try {
			JobClient.runJob(jobConf);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
