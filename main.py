from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_aws import ChatBedrock
from helpers.embedding_function import get_embedding_function
import defaults, warnings, argparse
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Suppress only UserWarnings
warnings.filterwarnings("ignore", category=UserWarning)

CHROMA_PATH = defaults.CHROMA_PATH
PROMPT_TEMPLATE = defaults.PROMPT_TEMPLATE
embedding_function = get_embedding_function()

def get_query(query_text):
    model = ChatBedrock(model_id = "anthropic.claude-instant-v1",
                    model_kwargs = {"temperature":0.4, "top_p":0.8})

    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=get_embedding_function())
    results = db.similarity_search_with_relevance_scores(query_text, k=5)
    sources = [doc.metadata for doc, _score in results]

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    print(prompt)

    response = model.invoke(prompt)
    response_text = response.content
    formatted_response = f"Response:\n{response_text}\n\nSources: {sources}"
    print(formatted_response)
    return formatted_response

# Telegram bot functions
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hi! Send me a query and I will process it for you.')

async def handle_message(update: Update, context: CallbackContext) -> None:
    if update.message.chat.type in ['group', 'supergroup']:
        bot_mention = f"@{context.bot.username}"
        if bot_mention in update.message.text:
            query_text = update.message.text.replace(bot_mention, '').strip()
            response = get_query(query_text)
            await update.message.reply_text(response)
    else:
        # Handle private messages
        query_text = update.message.text
        response = get_query(query_text)
        await update.message.reply_text(response)


def main():
    application = Application.builder().token("7405473302:AAG3DS_FmloS_rcCdauYrHnakMkf0PQGpyc").build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the Bot
    application.run_polling()

if __name__ == "__main__":
    main()

'''
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process a query using the RAG system.')
    parser.add_argument('query', type=str, help='The query text to be processed')
    args = parser.parse_args()
    get_query(args.query)
'''
