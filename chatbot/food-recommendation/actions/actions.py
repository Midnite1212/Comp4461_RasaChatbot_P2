from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

ALLOWED_FOOD_CATEGORIES = ["cuisine", "restriction", "calories", "diet", "healthy"]
ALLOWED_FOOD_TYPES = ["indian", "japanese", "korean", "western", "vegan", "glutten-free", "lose-weight", "body-building", "balanced"]
FOOD_IMAGES= [["https://www.tastingtable.com/img/gallery/20-japanese-dishes-you-need-to-try-at-least-once/intro-1664219638.jpg", "https://i.imgur.com/nGF1K8f.jpg"],
              
              [],
              
              [],
              
              [],
              
              [],
              
              [],
              
              [],
              
              []]

# 0: "indian", 
# 1: "japanese", 
# 2: "korean", 
# 3: "western", 
# 4: "vegan", 
# 5: "glutten-free", 
# 6: "lose-weight", 
# 7: "body-building", 
# 8: "balanced"

class ValidateSimpleFoodForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_food_recommendation_form"

    def validate_food_category(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `food_category` value."""

        if slot_value.lower() not in ALLOWED_FOOD_CATEGORIES:
            dispatcher.utter_message(text=f"We only accept food categories: cuisine / restriction diet / calories diet.")
            return {"food_category": None}
        dispatcher.utter_message(text=f"OK! You want to have {slot_value} food.")
        return {"food_category": slot_value}

    def validate_food_type(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `food_type` value."""

        if slot_value not in ALLOWED_FOOD_TYPES:
            dispatcher.utter_message(text=f"I don't recognize that food type. We serve {'/'.join(ALLOWED_FOOD_TYPES)}.")
            return {"food_type": None}
        dispatcher.utter_message(text=f"OK! You want to have {slot_value} food.")
        return {"food_type": slot_value, "food_img": FOOD_IMAGES[0][0]}
