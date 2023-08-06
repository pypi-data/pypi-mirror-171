use pyo3::prelude::*;

pub mod bagchal;
pub mod constants;
pub mod types;

use bagchal::BaghchalRS;
use types::*;

#[pyclass]
struct Baghchal {
    inner: BaghchalRS,
}

impl Default for Baghchal {
    fn default() -> Self {
        Self {
            inner: BaghchalRS::default(),
        }
    }
}

#[pymethods]
impl Baghchal {
    #[new]
    fn python_new(
        turn: Option<i8>,
        goat_counter: Option<i8>,
        goat_captured: Option<i8>,
        game_state: Option<GameStatus>,
        game_history: Option<Vec<GameStateInstance>>,
        pgn: Option<String>,
        prev_move: Option<Option<Move>>,
        move_reward_tiger: Option<Vec<f32>>,
        move_reward_goat: Option<Vec<f32>>,
        trapped_tiger: Option<i8>,
    ) -> PyResult<Self> {
        let mut obj = Self::default();

        if turn.is_some() {
            obj.inner.turn = turn.unwrap();
        };

        if goat_counter.is_some() {
            obj.inner.goat_counter = goat_counter.unwrap();
        };

        if goat_captured.is_some() {
            obj.inner.goat_captured = goat_captured.unwrap();
        };

        if game_state.is_some() {
            obj.inner.game_state = game_state.unwrap();
        };

        if game_history.is_some() {
            obj.inner.game_history = game_history.unwrap();
        };

        if pgn.is_some() {
            obj.inner.pgn = pgn.unwrap();
        };

        if prev_move.is_some() {
            obj.inner.prev_move = prev_move.unwrap();
        };

        if move_reward_tiger.is_some() {
            obj.inner.move_reward_tiger = move_reward_tiger.unwrap();
        };

        if move_reward_goat.is_some() {
            obj.inner.move_reward_goat = move_reward_goat.unwrap();
        };

        if trapped_tiger.is_some() {
            obj.inner.trapped_tiger = trapped_tiger.unwrap();
        };

        return Ok(obj);
    }

    pub fn board(&self) -> [[i8; 5]; 5] {
        return self.inner.board();
    }

    pub fn move_count(&self) -> i8 {
        return self.inner.move_count();
    }

    pub fn game_status_check(&self) -> GameStatusCheckResult {
        return self.inner.game_status_check();
    }

    pub fn turn(&self) -> i8 {
        return self.inner.turn;
    }

    pub fn goat_counter(&self) -> i8 {
        return self.inner.goat_counter;
    }

    pub fn goat_captured(&self) -> i8 {
        return self.inner.goat_captured;
    }

    pub fn game_state(&self) -> GameStatus {
        return self.inner.game_state;
    }

    pub fn game_history(&self) -> Vec<GameStateInstance> {
        return self.inner.game_history.clone();
    }

    pub fn pgn(&self) -> &str {
        return &self.inner.pgn;
    }

    pub fn prev_move(&self) -> Option<Move> {
        return self.inner.prev_move;
    }

    pub fn move_reward_tiger(&self) -> Vec<f32> {
        return self.inner.move_reward_tiger.clone();
    }

    pub fn trapped_tiger(&self) -> i8 {
        return self.inner.trapped_tiger;
    }

    pub fn move_reward_goat(&self) -> Vec<f32> {
        return self.inner.move_reward_goat.clone();
    }

    pub fn state_as_inputs(&self, possible_moves_pre: Option<Vec<PossibleMove>>) -> Vec<Vec<i8>> {
        return self.inner.state_as_inputs(possible_moves_pre);
    }

    pub fn clear_game(&mut self) {
        return self.inner.clear_game();
    }

    pub fn resign(&mut self, side: i8) -> GameStatusCheckResult {
        return self.inner.resign(side);
    }

    pub fn load_game(&mut self, pgn: String) {
        return self.inner.load_game(pgn);
    }

    pub fn make_move(
        &mut self,
        source: Option<[i8; 2]>,
        target: [i8; 2],
        eval_res: Option<MoveCheckResult>,
    ) -> MoveCheckResult {
        return self.inner.make_move(source, target, eval_res);
    }

    pub fn get_possible_moves(&self) -> Vec<PossibleMove> {
        return self.inner.get_possible_moves();
    }
}

#[pymodule]
fn libbaghchal(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Baghchal>()?;
    m.add_class::<MoveCheckResult>()?;
    m.add_class::<PossibleMove>()?;
    m.add_class::<GameStateInstance>()?;
    m.add_class::<GameStatusCheckResult>()?;
    Ok(())
}
