from services.prompt_builder import build_prompt
from services.gemini import generate_text


class AIService:

    async def create_prompt(
        self,
        product,
        background,
        style,
        text,
        price,
        old_price,
        discount,
    ):

        prompt = build_prompt(
            product=product,
            background=background,
            style=style,
            text=text,
            price=price,
            old_price=old_price,
            discount=discount,
        )

        return prompt

    async def generate(self, prompt):

        result = generate_text(prompt)

        return result
