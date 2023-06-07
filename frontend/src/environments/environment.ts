export const environment = {
  production: false,
  apiUrl: 'http://localhost:8000/api',
  linkedInClientId: 'your-linkedin-client-id',
  openAiApiKey: 'your-openai-api-key',
  jobCrawlInterval: 6 * 60 * 60 * 1000, // 6 hours in milliseconds
  autoApplyJobLimit: 5,
  applicationFrequencyLimit: 30 * 24 * 60 * 60 * 1000, // 30 days in milliseconds
  dailyApplicationLimit: 10
};