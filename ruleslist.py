from dataclasses import dataclass, field
from typing import List
from Rule import Rule
import json

@dataclass
class RulesList :
  filename : str
  rules : List[Rule] = field(default_factory=List)
  
  def readRules(self) -> None:
    try:
      with open(self.filename) as data:
        self.rules = json.load(data)
    except Exception as e:
      print(f'Error while reading {self.filename} : {e}')