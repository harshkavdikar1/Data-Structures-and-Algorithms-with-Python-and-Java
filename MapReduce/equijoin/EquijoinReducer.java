package equijoin;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.MapReduceBase;
import org.apache.hadoop.mapred.OutputCollector;
import org.apache.hadoop.mapred.Reducer;
import org.apache.hadoop.mapred.Reporter;

public class EquijoinReducer extends MapReduceBase implements Reducer<Text, Text, Text, Text>{

	@Override
	public void reduce(Text key, Iterator<Text> values, OutputCollector<Text, Text> output, Reporter reporter)
			throws IOException {
		ArrayList<String> first;
		HashSet<String> driver = new HashSet<String>();
		HashMap<String, ArrayList<String>> row_mapper = new HashMap<String, ArrayList<String>>();
		while (values.hasNext()){
			Text value = values.next();
			String row = value.toString();
			String sec_key = row.split(", ")[0];
			driver.add(sec_key);
			if (row_mapper.containsKey(sec_key)) {
				first = row_mapper.get(sec_key);
				first.add(row);
				row_mapper.replace(sec_key, first);
			}
			else {
				first = new ArrayList<String>();
				first.add(row);
				row_mapper.put(sec_key, first);
			}
		}
		Iterator<String> it = driver.iterator();
		String key1 = it.next();
		if (!it.hasNext()) {
			return;
		}
		else {
			String key2 = it.next();
			first = row_mapper.get(key1);
			ArrayList<String> second = row_mapper.get(key2);
			String temp = "";
			for (int i=0; i<first.size();i++) {
				String temp2 = "";
				for (int j=0; j<second.size(); j++) {
					temp2 += first.get(i) + " " + second.get(j) + "\n";
				}
				temp += temp2;
			}
			temp = temp.substring(0, temp.length() - 1);
			output.collect(null, new Text(temp));
		}
	}
}
