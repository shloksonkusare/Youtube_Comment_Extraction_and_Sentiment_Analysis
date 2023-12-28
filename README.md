# Youtube_Comment_Extraction_and_Sentiment_Analysis
YouTube comment extraction and sentiment analysis is the process of extracting comments from YouTube videos and analyzing their sentiment, or emotional tone. This can be done using machine learning algorithms to identify patterns in the text that indicate positive, negative, or neutral sentiment.<br>
This information can be used for a variety of purposes, such as:<br>
1. Understanding how viewers are reacting to a particular video or channel.
2. Identifying potential areas for improvement in content.
3. Targeting marketing and outreach efforts more effectively.

## Step-by-step flow of the project:
1. Extract the Comments of a YouTube video with the help of the YouTube Video ID and the YouTube API. The Extracted comments will get stored into a CSV File.
2. Divide the comments which will be read from the CSV File into the Three Sentimental Values.
3. Fitting the Specific Data into the DataFrame for the Training and Testing purpose.
4. Initialize the Machine Learning Models and Predict the Values for the Classification Report.
5. Compare the outputs of the Machine Learning Models with the help of various factors like Accuracy, Precision, F-1 Value and Recall Value.
6. Visualize the Output values with Graphs and Plots.

## Tools Used: 
1. **YouTube API Key**: API is used to extract the comments of a video with the help of _video ID_.
2. **Natural language Toolkit**: NLTK is used to import the Valence Aware Dictionary and Sentiment Reasoner to divide the comments based on their Sentiments.
3. **Scikit-Learn Library**: It is imported to use the Machine Learning models efficiently.
4. **Other Libraries**: This Includes Pandas, Matplotlib and Numpy for performing basic functions for the data and visualizing the output.

## Insights After Performing the Project:
1. Support Vector Machine Model provides the most accurate results amongst all models.
2. K-nearest Neighbors Model provides the least accurate results amongst all models.
3. Majority of the comments after categorized into Neutral sentimental value, followed by Positive value and Negative value resp.
4. We came to know that the comments of a Youtube video can be studied for understanding the human perception towards the video.
5. It helps how the content creators resonating with their audience, or identifying the areas of potential improvements.
6. The demographics of viewers who are expressing positive or negative sentiments. This information can be used to target marketing and outreach efforts more effectively.
7. This Project can be a potential tool that can be used for gaining valuable insights in public opinion.
8. This information can be used to improve content, make better business decisions, and inform public policy.
