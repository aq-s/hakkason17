from google.cloud import aiplatform
import google.generativeai as genai

client = aiplatform.gapic.PipelineServiceClient()

genai.configure(api_key="your-api-key-here")