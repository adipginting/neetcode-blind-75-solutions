use::std::collections::HashMap;
impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut hashmap_s: HashMap<char, i32> = HashMap::new();
        let mut hashmap_t: HashMap<char, i32> = HashMap::new();
        
        if (s.len() != t.len()){
            return false;
        }

        for ch in s.chars(){
            if let Some(number) = hashmap_s.get(&ch){
                hashmap_s.insert(ch, *number + 1);
            } else {
                hashmap_s.insert(ch, 1);
            }
        }
        for ch in t.chars(){
            if let Some(number) = hashmap_t.get(&ch){
                hashmap_t.insert(ch, *number + 1);
            } else {
                hashmap_t.insert(ch, 1);
            }
        }
        
        for ch in s.chars(){
            if let Some(number_s) = hashmap_s.get(&ch){
                if let Some (number_t) = hashmap_t.get(&ch){
                    if (*number_s == *number_t){
                        println!("{}", ch);
                        continue;
                    } else {
                        return false;
                    }
                } else {
                    return false;
                }
            }
        }
        return true;
    }
}
