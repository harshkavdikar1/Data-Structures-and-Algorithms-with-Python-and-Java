package CountryCount;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.MapReduceBase;
import org.apache.hadoop.mapred.Mapper;
import org.apache.hadoop.mapred.OutputCollector;
import org.apache.hadoop.mapred.Reporter;

public class CountryCountMapper extends MapReduceBase implements Mapper<LongWritable, Text, Text, IntWritable>{

	private static IntWritable one = new IntWritable(1);
	@Override
	public void map(LongWritable key, Text value, OutputCollector<Text, IntWritable> output, Reporter reporter)
			throws IOException {
		// TODO Auto-generated method stub
		String val = value.toString();
		String[] Data = val.split(",");
		output.collect(new Text(Data[7]), one);
	}

}
